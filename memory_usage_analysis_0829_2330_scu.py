# 代码生成时间: 2025-08-29 23:30:06
import psutil
import os
import gr

"""
A Python program to analyze memory usage using the Grap

This program uses the psutil library to get the memory usage
statistics and Gr to display them.
"""


def get_memory_usage():
    """Get the memory usage statistics of the current system."""
    try:
        # Get system memory usage
        mem = psutil.virtual_memory()
        return {
            'total': mem.total / (1024 ** 3),  # Total memory in GB
            'available': mem.available / (1024 ** 3),  # Available memory in GB
            'used': mem.used / (1024 ** 3),  # Used memory in GB
            'percentage': mem.percent  # Memory usage percentage
        }
    except Exception as e:
        # Handle exceptions
        print(f"Error getting memory usage: {e}")
        raise


def display_memory_usage(mem_stats):
    """Display the memory usage statistics using Gr."""
    try:
        # Create a Gr plot
        labels = ['Total', 'Available', 'Used']
        values = [mem_stats['total'], mem_stats['available'], mem_stats['used']]
        bars = gr.bar(labels, values)
        gr.show()
    except Exception as e:
        # Handle exceptions
        print(f"Error displaying memory usage: {e}")
        raise


def main():
    """Main function to analyze memory usage."""
    # Get memory usage statistics
    mem_stats = get_memory_usage()

    # Display memory usage statistics
    display_memory_usage(mem_stats)

if __name__ == '__main__':
    main()