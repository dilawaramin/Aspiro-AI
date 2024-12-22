"""_summary_
This module contains utility functions for the GPT API.
"""
import os
import datetime
import json


def store_message_json(message):
    """ 
    Store the message in the json file
    
    :param message: str: message to store
    :return: str: success message
    """
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = message.choices[0].message.content
    tokensUsed = message.usage.total_tokens
    
    print(f"""Data Extracted: 
          Time: {time}
          Content: {content}
          Tokens Used: {tokensUsed}""")
    
    # Get the directory of the current Python script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Script Directory: {script_dir}")

    # Path to the JSON file
    json_file_path = os.path.join(script_dir, "temp_data.json")
    print(f"JSON File Path: {json_file_path}")
    
    # Read the existing data or initialize an empty list
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("Error: JSONDecodeError")
                data = []
    else:
        print("Other Error")
        data = []
    
    # Append the new message
    data.append({
        "time": time,
        "content": content,
        "tokens_used": tokensUsed
    })
    
    # Write the updated data back to the file
    with open(json_file_path, "w") as f:
        json.dump(data, f, indent=4)    
        print("Message stored in temp_data.json")
    
    return "Message successfully stored"

    