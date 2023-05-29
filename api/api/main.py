from googletrans import Translator, constants

def translating_function(input):


    word_list = input.split()

    print(word_list)

    i = 0

    empty_array = []

    while i < len(word_list):
        translator = Translator()

        translation = translator.translate(word_list[i], src="de")

        empty_array.append(translation.text)

        i = i + 1
        # print(translator.detect("Hei jeg liker bønner"))

    sentence = " ".join(empty_array)

    print(sentence)
    return sentence

if __name__ == '__main__':
    translating_function("guten tag mein fuhrer")



