additionQuestions = [{'id': 1, 'name': 'Question 1', 'question': '7 + 3 = ?', 'options': [
    {'content': '2', 'selected': False}, {'content': '10', 'selected': False},
    {'content': '99', 'selected': False}, {'content': '122', 'selected': False}],
    'answer': '10', 'userAnswer': None},
    {'id': 2, 'name': 'Question 2', 'question': '4 + 7 = ?',
     'options': [
         {'content': '2', 'selected': False}, {
             'content': '11', 'selected': False},
         {'content': '31', 'selected': False}, {'content': '42', 'selected': False}],
     'answer': '11', 'userAnswer': None},
    {'id': 3, 'name': 'Question 3', 'question': '10 + 32 = ?', 'options': [
        {'content': '2', 'selected': False}, {
            'content': '42', 'selected': False},
        {'content': '61', 'selected': False}, {'content': '412', 'selected': False}],
        'answer': '42', 'userAnswer': None},
    {'id': 4, 'name': 'Question 4', 'question': '77 + 32 = ?', 'options': [
        {'content': '-24', 'selected': False}, {
            'content': '922', 'selected': False},
        {'content': '144', 'selected': False}, {'content': '109', 'selected': False}],
        'answer': '109', 'userAnswer': None},
    {'id': 5, 'name': 'Question 5', 'question': '17 + 23 = ?', 'options': [
        {'content': '55', 'selected': False}, {
            'content': '40', 'selected': False},
        {'content': '19', 'selected': False}, {'content': '2', 'selected': False}],
     'answer': '40', 'userAnswer': None}]

subtractionQuestions = [{'id': 1, 'name': 'Question 1', 'question': '11 - 5 = ?', 'options': [
    {'content': '-2', 'selected': False}, {'content': '2', 'selected': False},
    {'content': '6', 'selected': False}, {'content': '15', 'selected': False}],
    'answer': '6', 'userAnswer': None},
    {'id': 2, 'name': 'Question 2', 'question': '99 - 7 = ?',
     'options': [
         {'content': '111', 'selected': False}, {
             'content': '92', 'selected': False},
         {'content': '314', 'selected': False}, {'content': '-32', 'selected': False}],
     'answer': '92', 'userAnswer': None},
    {'id': 3, 'name': 'Question 3', 'question': '55 - 32 = ?', 'options': [
        {'content': '23', 'selected': False}, {
            'content': '36', 'selected': False},
        {'content': '42', 'selected': False}, {'content': '412', 'selected': False}],
        'answer': '23', 'userAnswer': None},
    {'id': 4, 'name': 'Question 4', 'question': '17 - 4 = ?', 'options': [
        {'content': '88', 'selected': False}, {
            'content': '5', 'selected': False},
        {'content': '13', 'selected': False}, {'content': '14', 'selected': False}],
        'answer': '13', 'userAnswer': None},
    {'id': 5, 'name': 'Question 5', 'question': '30 - 9 = ?', 'options': [
        {'content': '31', 'selected': False}, {
            'content': '21', 'selected': False},
        {'content': '11', 'selected': False}, {'content': '22', 'selected': False}],
        'answer': '21', 'userAnswer': None}]

results = {'additionQuiz': {'correct': 0,
                            'correctQuestions': [], 'wrong': 0, 'wrongQuestions': [], 'score': 0},
           'subtractionQuiz': {'correct': 0,
                               'correctQuestions': [], 'wrong': 0, 'wrongQuestions': [], 'score': 0}}

practice_questions = {
    'addition': [
        {'id': 1, 'options': [7, 5, 3, 11, None],
            'answer': '3', 'userAnswer': None},
        {'id': 2, 'options': [9, 2, 11, 5, None],
            'answer': '5', 'userAnswer': None},
        {'id': 3, 'options': [2, 12, 7, 5, None],
            'answer': '2', 'userAnswer': None},
        {'id': 4, 'options': [7, 6, 41, 33, None],
            'answer': '7', 'userAnswer': None},
    ],
    'subtraction': [
        {'id': 1, 'options': [3, 1, 33, 11, None],
            'answer': '1', 'userAnswer': None},
        {'id': 2, 'options': [1, 8, 0, 25, None],
            'answer': '0', 'userAnswer': None},
        {'id': 3, 'options': [6, 2, 97, 1, None],
            'answer': '2', 'userAnswer': None},
        {'id': 4, 'options': [15, 2, 27, 32, None],
            'answer': '2', 'userAnswer': None},
    ]
}
