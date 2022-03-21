import json

__candidates = []


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    global __candidates
    with open(path, 'r', encoding='utf-8') as file:
        __candidates = json.load(file)
    return __candidates


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    candidate = __candidates[candidate_id - 1]
    return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidate_list_names = []
    for candidate in __candidates:
        if candidate_name.lower() in candidate['name'].lower():
            candidate_list_names.append(candidate)
    return candidate_list_names


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    candidate_list_skills = []
    for candidate in __candidates:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidate_list_skills.append(candidate)
    return candidate_list_skills

