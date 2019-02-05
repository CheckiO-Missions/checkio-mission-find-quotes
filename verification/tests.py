"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['"Greetings"'],
            "answer": ['Greetings']
        },
        {
            "input": ['Hi'],
            "answer": []
        },
        {
            "input": ['good morning mister "superman"'],
            "answer": ['superman']
        },
        {
            "input": ['"this" doesn\'t make any "sense"'],
            "answer": ['this', 'sense']
        },
        {
            "input": ['"Lorem Ipsum" is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the "industry\'s standard dummy text ever since the 1500s", when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. "It was popularised in the 1960s" with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'],
            "answer": [
                'Lorem Ipsum',
                "industry\'s standard dummy text ever since the 1500s",
                'It was popularised in the 1960s']
        },
        {
            "input": ['count empty quotes ""'],
            "answer": ['']
        }
    ],
    "Extra": [
        {
            "input": ['Well done, my "friend"'],
            "answer": ['friend']
        },

        {
            "input": ["Well done, my 'friend'"],
            "answer": []
        }
    ]
}
