import argparse
import json
import google.generativeai as genai

# Setting up an API Key and model for the script (here Gemma 3)
genai.configure(api_key="AIzaSyBTFG8MfNleu2DfQSuJgzSMpTgKBNVtjco")
model = genai.GenerativeModel('gemma-3-27b-it')

def get_prompt_response(prompt):

    api_response = model.generate_content(prompt)
    # We need the text field from the response
    output = api_response.text
    print(f"Response for {prompt}: {output}")
    print("--------------------------------")
    return output

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", default='text.txt', help="Path to text file with prompts.",)
    parser.add_argument("--output_path", default='llm_outputs.json', help="Path to save JSON responses.")

    args = parser.parse_args()

    input_prompts = []
    with open(args.input_path, "r") as file:
        for line in file:
            # reading each line of the file
            input_prompts.append(line)

    output_list = []
    # Saving the mapping of input and output as dict
    for prompt in input_prompts:
        output = get_prompt_response(prompt)
        output_dict = {'prompt':prompt,'response':output}
        output_list.append(output_dict)

    with open(args.output_path, "w") as file:
        # Save the outputs as a json object
        json.dump(output_list, file, indent=2)

if __name__ == "__main__":
    main()