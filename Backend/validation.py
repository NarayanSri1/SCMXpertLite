# importing HTTPexception
import re
from fastapi import HTTPException
from models import user


def validation(User:user):
    password_regex="((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})"
    user_password=User.password
    compile=re.compile(password_regex)
    search=re.search(compile,user_password)

    if not search:
        raise HTTPException(
            status_code=400,detail="Invalid Password."
        )
    return search
