import json

def questionsToJson(questions):
    # Converts questions json string to key value object
    questions_dict = json.loads(questions)
    return questions_dict

questions = """{
                        "questions": [
                            {
                                "question": "What type of cuisine does Thai Korner specialize in?",
                                "answers": [
                                    {"text": "Authentic Thai cuisine", "correct": true},
                                    {"text": "Fusion Thai cuisine", "correct": false},
                                    {"text": "Traditional Chinese cuisine", "correct": false},
                                    {"text": "Modern Thai cuisine", "correct": false}
                                ]
                            },
                            {
                                "question": "Where is one of the locations of Thai Korner?",
                                "answers": [
                                    {"text": "Shop 24/1 Commercial Road, Upper Coomera", "correct": true},
                                    {"text": "Shop 15/2 Main Street, Upper Coomera", "correct": false},
                                    {"text": "Shop 27/102 Pimpama Jacobs Well Road", "correct": false},
                                    {"text": "Shop 10/50 Pimpama Road", "correct": false}
                                ]
                            },
                            {
                                "question": "What are the opening hours for Thai Korner on weekends?",
                                "answers": [
                                    {"text": "11:00 AM to 9:00 PM", "correct": true},
                                    {"text": "10:00 AM to 8:00 PM", "correct": false},
                                    {"text": "12:00 PM to 10:00 PM", "correct": false},
                                    {"text": "11:30 AM to 9:30 PM", "correct": false}
                                ]
                            },
                            {
                                "question": "Which of the following menu options does Thai Korner offer?",
                                "answers": [
                                    {"text": "Vegetarian and gluten-free dishes", "correct": true},
                                    {"text": "Only meat-based dishes", "correct": false},
                                    {"text": "Seafood only dishes", "correct": false},
                                    {"text": "Desserts only", "correct": false}
                                ]
                            },
                            {
                                "question": "What is one of the desserts available at Thai Korner?",
                                "answers": [
                                    {"text": "Mango Sticky Rice", "correct": true},
                                    {"text": "Chocolate Lava Cake", "correct": false},
                                    {"text": "Cheesecake", "correct": false},
                                    {"text": "Tiramisu", "correct": false}
                                ]
                            }
                        ]
                    }"""

questionsToJson(questions)