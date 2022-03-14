# lIST & TUPLE & Dictionary

# List와 관련 연산자
catfoods = ["참치","연어","닭","북어","도미"]
print(type(catfoods))
print("새우" in catfoods) #결과:False
print(catfoods[0]) #참치
print(len(catfoods)) #list의 길이 return #결과:5
# catfoods.append 전에 print(len...)이 실행되었으므로 6이 아닌 5 반환
catfoods.append("게살")
print(catfoods)
catfoods.reverse() #item들을 역순으로 정렬
print(catfoods)

# Tuple
rainbow = ("빨","주","노","초","파","남","보")
print(type(rainbow))
# rainbow.append("핑크")
# 불변 시퀀스에 가변 연산자를 사용했으므로 에러 출

# Dictionary(mapping type=mapping object)
Butler = {
    "Name" : "PawPaw",
    "Cat" : True,
    "Cat age" : 5,
    "Job" : ["feed","clean toilet","play","give medicine"],
    "Tuple" : (1,2,3),
} # Key를 쓸 때 따옴표를 꼭 써줄 것!
print(type(Butler))
print(Butler["Cat age"]) #5
Butler["Cat Name"]="Paw" # 새로운 쌍 추가 가능!
print(Butler)
