class Report: 
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        return f"{self.title}\n\n{self.content}"

class ReportSaver:
    def __init__(self, report: Report, filename):
        self.report = report
        self.filename = filename
        
        def save_to_file(self):
            with open(self.filename, 'w') as file:
                file.write(self.report.generate_report())

relatorio = Report("Relatório de Vendas", "Este é o conteúdo do relatório de vendas.")
mostrar_na_tela = relatorio.generate_report()

salvar_relatorio = ReportSaver(relatorio, "relatorio.pdf")
salvar_relatorio.save_to_file()