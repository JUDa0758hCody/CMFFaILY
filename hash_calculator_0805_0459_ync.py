# 代码生成时间: 2025-08-05 04:59:26
import hashlib
import gr

class HashCalculator:
    """
    A tool to calculate hash values using various algorithms.
    """

    def __init__(self):
        # Supported hash algorithms
        self.supported_algorithms = ['md5', 'sha1', 'sha256', 'sha512']

    def calculate_hash(self, input_data, algorithm='sha256'):
        """
        Calculate the hash value for the given input data.

        Args:
            input_data (str): Data to calculate hash.
            algorithm (str, optional): Hash algorithm to use. Defaults to 'sha256'.

        Returns:
            str: The calculated hash value.
        """
        if algorithm not in self.supported_algorithms:
            raise ValueError(f'Unsupported algorithm: {algorithm}. Supported algorithms are: {self.supported_algorithms}')

        try:
            # Create a new hash object
            hash_object = getattr(hashlib, algorithm)()
            # Update the hash object with the input data
            hash_object.update(input_data.encode('utf-8'))
            # Return the hexadecimal representation of the hash value
            return hash_object.hexdigest()
        except Exception as e:
            # Handle any unexpected errors
            print(f'An error occurred: {e}')
            return None

    def run(self):
        """
        Set up the Gradio interface and run the application.
        """
        # Create the Gradio interface
        gr.Interface(
            fn=self.calculate_hash,
            inputs=gr.Textbox(label='Input data'),
            outputs='text',
            title='Hash Calculator Tool',
            description='A tool to calculate hash values for input data.'
        ).launch()

if __name__ == '__main__':
    # Create an instance of the HashCalculator class
    calculator = HashCalculator()
    # Run the Gradio interface
    calculator.run()