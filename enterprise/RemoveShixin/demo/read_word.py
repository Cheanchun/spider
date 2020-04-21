from docx import Document

word = Document("07.docx")   # todo doing
for paragraph in word.paragraphs:
    text = paragraph.text
    if "关于" in text or "公告" in text:
        print(text)
        print("=====")
        with open("./title.txt", "a+", encoding="utf-8") as fp:
            fp.write(text + "\n")
    if "统一社会信用代码/注册号" in text:
        print(text)
        print("-----")
