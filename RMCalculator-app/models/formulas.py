# --- SQ(RM換算)関数 ---
def calc_sq(lifting_weight,reps):
    rm=lifting_weight*reps/33.3+lifting_weight
    return round(rm,0)

# --- DL(RM換算)関数 ---
def calc_dl(lifting_weight,reps):
    rm=lifting_weight*reps/33.3+lifting_weight
    return round(rm,0)

# --- BP(RM換算)関数 ---
def calc_bp(lifting_weight,reps):
    rm=lifting_weight*reps/40+lifting_weight
    return round(rm,0)

FORMULAS = {
    "SQ": calc_sq,
    "DL": calc_dl,
    "BP": calc_bp,
}