import win32com.client 

def refresh_excel_data_connections(file_paths):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.DisplayAlerts = False  # Disable alerts and confirmation prompts
    excel.Visible = False  # Set to True if you want to see the Excel window, False otherwise
    for file_path in file_paths:
        try:
            workbook = excel.Workbooks.Open(file_path)
        
            # Refresh all data connections
            for connection in workbook.Connections:
                connection.Refresh()

            # Save and close the workbook
            workbook.Save()
            workbook.Close()
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    # Quit Excel application
    excel.Quit()

if __name__ == "__main__":
    file_paths = [
        "C:\\Users\\REPRO SANDRO\\Documents\\DASHBOARD FV\\SETORES\\DASHBOARD_SETOR1.xlsx",
        "C:\\Users\\REPRO SANDRO\\Documents\\DASHBOARD FV\\SETORES\\DASHBOARD_SETOR2.xlsx",
        "C:\\Users\\REPRO SANDRO\\Documents\\DASHBOARD FV\\SETORES\\DASHBOARD_SETOR3.xlsx",
        "C:\\Users\\REPRO SANDRO\\Documents\\DASHBOARD FV\\SETORES\\DASHBOARD_SETOR4.xlsx",
        "C:\\Users\\REPRO SANDRO\\Documents\\DASHBOARD FV\\SETORES\\DASHBOARD_SETOR5.xlsx",
        "C:\\Users\\REPRO SANDRO\\Documents\\DASHBOARD FV\\SETORES\\DASHBOARD_SETOR6.xlsx",
        "C:\\Users\\REPRO SANDRO\\Documents\\DASHBOARD FV\\SETORES\\DASHBOARD_SETOR7.xlsx"
    ]
    refresh_excel_data_connections(file_paths)


