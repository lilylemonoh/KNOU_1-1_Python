# 원뿔 계산 프로그램 개선
# 사용자로부터 반지름과 높이를 입력받고 계산

# 반지름 사용자 입력
rad = int(input("반지름을 입력하세요:"))
# 높이 사용자 입력
hei = int(input("높이를 입력하세요:"))
#부피 & 겉넓이 계산
vol = 1/3 * 3.14 * rad ** 2 * hei
suf = 3.24 * rad ** 2 + 3.14 * rad * hei
print(vol)
print(suf)