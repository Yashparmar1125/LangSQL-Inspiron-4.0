import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re
import json

# Assuming your original code is in a file called text_to_sql_feedback.py
# Import functions or copy the code here
# For this example, I'll include the essential parts:

# Load model & tokenizer (you only need to do this once)
tokenizer = AutoTokenizer.from_pretrained("gaussalgo/T5-LM-Large-text2sql-spider")
model = AutoModelForSeq2SeqLM.from_pretrained("gaussalgo/T5-LM-Large-text2sql-spider")
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Create a FeedbackManager instance (copied from your code)
# (I'm including a simplified version for testing)
class FeedbackManager:
    def _init_(self):
        self.reset_session()
        
        # Define feedback categories and related keywords
        self.feedback_categories = {
            "missing_fields": ["missing", "include", "add", "without", "need", "should have"],
            "optimization": ["optimize", "slow", "faster", "performance", "efficient", "simpler"],
            "incorrect_results": ["incorrect", "wrong", "error", "not right", "invalid", "different"],
            "join_issues": ["join", "relation", "connection", "link", "association"],
            "filter_issues": ["filter", "where", "condition", "constraint"],
            "grouping_issues": ["group", "aggregate", "summarize"],
            "sorting_issues": ["sort", "order", "arrange"]
        }
        
        # NLP patterns to extract field names
        self.field_extraction_patterns = [
            r"missing (?:the |)(\w+)(?: field| column|)",
            r"include (?:the |)(\w+)",
            r"add (?:the |)(\w+)",
            r"without (?:the |)(\w+)",
            r"need (?:the |)(\w+)"
        ]
        
    def reset_session(self):
        """Reset the session data to its initial state"""
        self.session_data = {
            "missing_fields": [],
            "extra_fields": [],
            "optimization": False,
            "incorrect_results": False,
            "join_issues": False,
            "filter_issues": [],
            "grouping_issues": False,
            "sorting_issues": [],
            "previous_queries": [],
            "feedback_history": [],
            "custom_directives": []
        }
    
    def capture_feedback(self, feedback_text, original_query):
        # Implementation of capture_feedback (simplified for testing)
        self.session_data["feedback_history"].append({
            "feedback": feedback_text,
            "query": original_query,
            "timestamp": None
        })
        
        # Store previous query for reference
        self.session_data["previous_queries"].append(original_query)
        
        # Convert feedback to lowercase for easier matching
        feedback_lower = feedback_text.lower()
        
        # Simple detection based on keywords
        for category, keywords in self.feedback_categories.items():
            for keyword in keywords:
                if keyword in feedback_lower:
                    if category == "missing_fields":
                        for pattern in self.field_extraction_patterns:
                            matches = re.findall(pattern, feedback_lower)
                            for match in matches:
                                if match and match not in self.session_data["missing_fields"]:
                                    self.session_data["missing_fields"].append(match)
                    else:
                        self.session_data[category] = True
        
        return self.session_data
    
    def format_input_with_feedback(self, question, schema):
        # Format the input for the model with feedback-based enhancements
        input_text = f"{schema} {question}"
        
        # Add simple feedback context
        if self.session_data["missing_fields"]:
            fields_list = ", ".join(self.session_data["missing_fields"])
            input_text += f" Include fields: {fields_list}."
            
        if self.session_data["optimization"]:
            input_text += " Optimize this query."
            
        if self.session_data["sorting_issues"]:
            input_text += " Apply proper sorting."
            
        return input_text

# Text to SQL function
def text_to_sql_with_feedback(question, schema, feedback_manager):
    # Format input with feedback
    input_text = feedback_manager.format_input_with_feedback(question, schema)
    
    # Tokenize the input
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)
    
    # Generate SQL query
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=256, num_beams=5, early_stopping=True)
    
    # Decode the generated SQL query
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
    return sql_query

# Process query with feedback
def process_query_with_feedback(question, schema, user_feedback=None, previous_query=None):
    # Create feedback manager if this is a new session
    if not hasattr(process_query_with_feedback, "feedback_manager"):
        process_query_with_feedback.feedback_manager = FeedbackManager()
    
    # Apply feedback if provided
    if user_feedback and previous_query:
        process_query_with_feedback.feedback_manager.capture_feedback(user_feedback, previous_query)
    
    # Generate SQL query with feedback-enhanced input
    sql_query = text_to_sql_with_feedback(question, schema, process_query_with_feedback.feedback_manager)
    
    return sql_query

# Function to reset the feedback session
def reset_feedback_session():
    if hasattr(process_query_with_feedback, "feedback_manager"):
        process_query_with_feedback.feedback_manager.reset_session()
    else:
        process_query_with_feedback.feedback_manager = FeedbackManager()
    return "Feedback session has been reset."

# Your schema in the format your model expects
schema = '"django_content_type" "id" integer , "app_label" character varying , "model" character varying , primary key: "id" [SEP] "auth_permission" "id" integer , "content_type_id" integer , "name" character varying , "codename" character varying , primary key: "id" , "content_type_id" [SEP] "auth_group" "id" integer , "name" character varying , primary key: "id" [SEP] "auth_group_permissions" "id" bigint , "group_id" integer , "permission_id" integer , primary key: "id" , "group_id" , "permission_id" [SEP] "registered_faces" "user_id" text , "name" text , "face_encoding" text , primary key: "user_id" [SEP] "visitors" "visitor_id" integer , "visit_date" timestamp without time zone , "name" text , "face_encoding" text , primary key: "visitor_id" [SEP]'

test_cases = [
    {
        "name": "Basic visitor query with ID filter",
        "question": "*Question:* Retrieve the names of all visitors with visitor_id greater than 100.",
        "feedback": None,
        "previous_query": None
    },
    {
        "name": "Visitor query with ordering feedback",
        "question": "*Question:* Retrieve the names of all visitors with visitor_id greater than 100.",
        "feedback": "Please order the results by name",
        "previous_query": "SELECT name FROM visitors WHERE visitor_id > 100"
    },
    {
        "name": "Visitor query with additional fields feedback",
        "question": "*Question:* Retrieve the names of all visitors with visitor_id greater than 100.",
        "feedback": "Include the visitor_id and visit_date in the results",
        "previous_query": "SELECT name FROM visitors WHERE visitor_id > 100 ORDER BY name"
    },
    {
        "name": "Visitor query with LIKE pattern",
        "question": "*Question:* Find all visitors whose names start with 'A'.",
        "feedback": None,
        "previous_query": None,
        "reset_session": True
    },
    {
        "name": "Aggregation query",
        "question": "*Question:* Count the total number of visitors.",
        "feedback": None,
        "previous_query": None,
        "reset_session": True
    },
    {
        "name": "Registered faces query",
        "question": "*Question:* List all registered users and their names.",
        "feedback": None,
        "previous_query": None,
        "reset_session": True
    },
    {
        "name": "Complex query with joins",
        "question": "*Question:* Find visitors who have the same name as registered users.",
        "feedback": None,
        "previous_query": None,
        "reset_session": True
    },
    {
        "name": "Complex query with optimization feedback",
        "question": "*Question:* Find visitors who have the same name as registered users.",
        "feedback": "Optimize this query and include visit_date in results",
        "previous_query": "SELECT v.name, r.user_id FROM visitors v JOIN registered_faces r ON v.name = r.name"
    },
    {
        "name": "Top N query",
        "question": "*Question:* List the top 5 visitors with the highest visitor_id.",
        "feedback": None,
        "previous_query": None,
        "reset_session": True
    },
    {
        "name": "Group by query",
        "question": "*Question:* Count how many visitors have the same name.",
        "feedback": None,
        "previous_query": None,
        "reset_session": True
    },
    {
        "name": "Group by with feedback",
        "question": "*Question:* Count how many visitors have the same name.",
        "feedback": "Sort the results by count in descending order",
        "previous_query": "SELECT name, COUNT(*) as count FROM visitors GROUP BY name"
    }
]

# Run the tests
def run_tests():
    print("Starting Text-to-SQL with Feedback Testing\n")
    
    for i, test in enumerate(test_cases):
        print(f"\n--- Test {i+1}: {test['name']} ---")
        
        # Reset session if needed
        if test.get("reset_session", False):
            print("Resetting feedback session...")
            reset_feedback_session()
        
        # Process the query
        print(f"Question: {test['question']}")
        
        if test['feedback'] is not None:
            print(f"Feedback: {test['feedback']}")
            print(f"Previous query: {test['previous_query']}")
        
        # Generate SQL
        try:
            sql_query = process_query_with_feedback(
                test['question'], 
                schema, 
                test['feedback'], 
                test['previous_query']
            )
            print(f"\nGenerated SQL Query:\n{sql_query}\n")
        except Exception as e:
            print(f"Error generating SQL: {str(e)}")

# Run the tests
if _name_ == "_main_":
    run_tests()