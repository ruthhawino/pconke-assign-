#No 1
# A function named concatenate_args that takes any number
# of string arguments in positional arguments format
# and concatenates them into a single string
def concatenate_args(*strings):
    result=" "
    for string in strings:
     result+=string
    return result
# A function named concatenate_kwargs that takes any number of string arguments
# in keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**words):
    answer=(" ")
    for key,value in words.items():
        answer+=(f"{key,value}")
    return answer  