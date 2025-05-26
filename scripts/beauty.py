import json
import os

def pretty_json_from_file(file_path, indent=4, save_to_file=True):
    """
    Reads a JSON file, pretty-prints its content, and optionally saves it to a new file.

    Args:
        file_path (str): The path to the JSON file.
        indent (int): The number of spaces to use for indentation (default is 4).
        save_to_file (bool): Whether to save the formatted JSON to a new file (default is True).

    Returns:
        str: A pretty-printed JSON string, or the original content if parsing fails.
             Returns None if the file cannot be read.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                pretty_json = json.dumps(data, indent=indent, ensure_ascii=False)
                
                if save_to_file:
                    # Create new file path
                    file_dir = os.path.dirname(file_path)
                    file_name = os.path.basename(file_path)
                    name, ext = os.path.splitext(file_name)
                    new_file_path = os.path.join(file_dir, f"{name}_pretty{ext}")
                    
                    # Save to new file
                    with open(new_file_path, 'w', encoding='utf-8') as out_file:
                        out_file.write(pretty_json)
                    print(f"Formatted JSON saved to: {new_file_path}")
                
                return pretty_json
            except json.JSONDecodeError:
                print(f"Error: Invalid JSON format in file: {file_path}")
                # Optionally return the original content of the file
                f.seek(0)
                return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

# Example usage:
file_path = '/home/lzq/LLMxMapReduce/LLMxMapReduce_V2/output/Bias and Fairness in LLMs_20250507_014104_crawl_result.jsonl'  # Replace with the actual path to your JSON file
pretty_output = pretty_json_from_file(file_path)

if pretty_output:
    print(pretty_output)