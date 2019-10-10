#Если значение выражения истинно,
#то в консоли не должно появиться дополнительных сообщений (в днном случае Message for user)
assert abs(-42)==-42, "Message for user"

#Форматирование строк
print("Let's count together! {}, then goes {}, and then {}".format("one", "two", "three"))

str1 = "one"
str2 = "two"
str3 = "third"
print(f"Let's count together! {str1}, then goes {str2}, and then {str3}")


def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result,"expected " + str(expected_result) + ", got " + str(actual_result)

    def test_substring(full_string, substring):
    assert substring in  full_string,"expected '" + str(substring) + "' to be substring of '" + str(full_string) + "'"
