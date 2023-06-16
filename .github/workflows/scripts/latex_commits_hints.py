if __name__ == "__main__":
    with open('lint_error.txt', 'r') as f:
        filecont = f.readlines()

    res = []
    line_found = False
    tmp_str = ""
    for line in filecont:
        if '.tex line ' in line:
            res.append(tmp_str)
            line_found = True
            tmp_str = ""
            tmp_str += line

        else:
            line_found = False
            tmp_str += line

    for elem in res:
        print(elem)
        print()

    with open('out_error.txt', 'w') as f:
        f.writelines('### Latex Warnings and Errors 🔍 \n')
        f.writelines(
            "Monello, sembra che tu non abbia rispettato il volere del potentissimo compilatore **ChkTek** !!\n"
        )
        f.writelines(
            'Di seguito trovi tutte le imprecisioni che dovresti correggere\n\n'
        )
        for line in res[1:]:
            f.writelines(f"- [ ] :warning: `{line}`\n")
            # f.writelines("\n\n")
