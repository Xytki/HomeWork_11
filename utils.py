import json
from candidate import Candidates


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    arr = []
    for item in data:
        candidate = Candidates(item['id'], item['name'], item['picture'], item['position'], item['gender'],
                               item['age'], item['skills'])
        arr.append(candidate)
    return arr


def get_candidate(candidate_id: int, arr: list) -> Candidates:
    """возвращает одного кандидата по его id"""

    for item in arr:
        if item.id == candidate_id:
            return item


def get_candidates_by_name(candidate_name: str, arr: list) -> Candidates:
    """возвращает кандидатов по имени"""

    ret_arr = []
    for item in arr:
        if candidate_name.lower() in item.name.lower():
            ret_arr.append(item)
    return ret_arr


def get_candidates_by_skill(skill_name: str, arr: list) -> Candidates:
    """возвращает кандидатов по навыку"""

    ret_arr = []
    for item in arr:
        if skill_name.lower() in item.skills.lower():
            ret_arr.append(item)
    return ret_arr







