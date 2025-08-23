# 代码生成时间: 2025-08-24 00:07:15
import random
import gr

# RandomNumberGenerator class
class RandomNumberGenerator:
    def __init__(self, min_value=1, max_value=100, lower_bound=True):
        """
        Initializes the random number generator with specified range.
        :param min_value: The minimum value of the range (inclusive)
        :param max_value: The maximum value of the range (inclusive)
        :param lower_bound: Whether the minimum value is inclusive
        """
        self.min_value = min_value
        self.max_value = max_value
        self.lower_bound = lower_bound
        
    def generate(self):
        """
        Generates a random number between min_value and max_value.
        :returns: A random integer within the specified range.
        :raises ValueError: If the min_value is greater than max_value.
        """
        if self.min_value > self.max_value:
            raise ValueError("Minimum value cannot be greater than maximum value.")
        return random.randint(self.min_value, self.max_value)

# Create a Gradio interface for the random number generator
def create_gradio_interface():
    """
    Creates a Gradio interface for generating random numbers.
    """
    generator = RandomNumberGenerator()
    input = gr.inputs.Slider(minimum=1, maximum=100, value=1, step=1, label="Minimum value")
    output = gr.outputs.Textbox()
    
    # Callback function to generate a random number
    def generate_random_number(min_value):
        return str(generator.generate())
    
    # Create the Gradio app
    app = gr.Interface(
        fn=generate_random_number, 
        inputs=input, 
        outputs=output,
        title="Random Number Generator"
    )
    
    # Launch the Gradio app
    app.launch()

# Run the Gradio interface
if __name__ == "__main__":
    create_gradio_interface()
