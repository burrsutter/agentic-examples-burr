from pydantic import Field
from sympy import sympify

from atomic_agents.agents.base_agent import BaseIOSchema
from atomic_agents.lib.base.base_tool import BaseTool, BaseToolConfig


################
# INPUT SCHEMA #
################
class CalculatorToolInputSchema(BaseIOSchema):
    """
    Tool for performing calculations. Supports basic arithmetic operations
    like addition, subtraction, multiplication, and division, as well as more
    complex operations like math fractions.
    Use this tool to evaluate mathematical expressions.
    """

    expression: str = Field(..., description="Strictly valid mathematical expression. Must be a valid arithmetic or symbolic expression, e.g., '2 + 2' or 'sin(pi/2)'. Avoid natural language or descriptive text such as units like 'meters', 'km/h', or 'seconds'; instead, convert them to numeric values before evaluation. Ensure logically correct operator precedence.")


#################
# OUTPUT SCHEMA #
#################
class CalculatorToolOutputSchema(BaseIOSchema):
    """
    Schema for the output of the CalculatorTool.
    """

    result: str = Field(..., description="Result of the calculation.")


#################
# CONFIGURATION #
#################
class CalculatorToolConfig(BaseToolConfig):
    """
    Configuration for the CalculatorTool.
    """

    pass


#####################
# MAIN TOOL & LOGIC #
#####################
class CalculatorTool(BaseTool):
    """
    Tool for performing calculations based on the provided mathematical expression.

    Attributes:
        input_schema (CalculatorToolInputSchema): The schema for the input data.
        output_schema (CalculatorToolOutputSchema): The schema for the output data.
    """

    input_schema = CalculatorToolInputSchema
    output_schema = CalculatorToolOutputSchema

    def __init__(self, config: CalculatorToolConfig = CalculatorToolConfig()):
        """
        Initializes the CalculatorTool.

        Args:
            config (CalculatorToolConfig): Configuration for the tool.
        """
        super().__init__(config)

    def run(self, params: CalculatorToolInputSchema) -> CalculatorToolOutputSchema:
        """
        Executes the CalculatorTool with the given parameters.

        Args:
            params (CalculatorToolInputSchema): The input parameters for the tool.

        Returns:
            CalculatorToolOutputSchema: The result of the calculation.
        """
        # Convert the expression string to a symbolic expression
        #parsed_expr = sympify(str(params.expression))
        try:
            parsed_expr = sympify(str(params.expression))
        except Exception as e:
            raise ValueError(f"Invalid mathematical expression provided: {params.expression}") from e

        # Evaluate the expression numerically
        result = parsed_expr.evalf()
        return CalculatorToolOutputSchema(result=str(result))


#################
# EXAMPLE USAGE #
#################
if __name__ == "__main__":
    calculator = CalculatorTool()
    result = calculator.run(CalculatorToolInputSchema(expression="sin(pi/2) + cos(pi/4)"))
    print(result)  # Expected output: {"result":"1.70710678118655"}
