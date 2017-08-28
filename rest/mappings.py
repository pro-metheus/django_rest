def get_uname(user):
    return user.username

def get_pass(user):
    return user.password


mapping={
'a':get_uname,
'b':get_pass

}
