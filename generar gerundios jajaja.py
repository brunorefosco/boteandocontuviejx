txt_verbos = open("verbos-espanol-conjugaciones.txt", "r", encoding='utf-8')
txt_gerundios = open("gerundios.txt", "a+", encoding='utf-8')

verbos = txt_verbos.readlines()
txt_verbos.close()

for v in verbos:
    if v.endswith('ndo', 0, len(v) - 1):
        txt_gerundios.write(v)

txt_gerundios.close()
print("escrito en la verga esa")
