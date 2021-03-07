# 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.
#
# 예) httop://naver.com
#
# 규칙 1 : http:// 부분은 제외 ⇒ naver.com
#
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 ⇒ naver
#
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#
# 예) 생성된 비밀번호 : nav51!

url = "http://shinhanfp.co.kr"
my_str = url.replace("http://", "")
print(my_str)

my_str = my_str[:my_str.index(".")]
print(my_str)  # 첫번째.이 나오는 5번째 까지의 수를 출력

password = my_str[:3] + str(len(my_str))+str(my_str.count("n"))+"!"
print("{0}의 비밀번호는 {1}입니다." .format(url, password))
