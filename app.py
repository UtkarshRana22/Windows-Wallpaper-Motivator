import jinja2,ctypes,os,base64,random
from html2image import Html2Image
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import datetime,json,random




date_entry=''
from datetime import datetime

def days_left_until(target_date_str):
    # Parse the target date from string to a datetime object
    target_date = datetime.strptime(target_date_str, '%Y-%m-%d')
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the difference between the target date and the current date
    delta = target_date - current_date
    
    # Return the number of days left
    return delta.days
from datetime import datetime

def days_passed_since(start_date_str):
    
    # Parse the start date from string to a datetime object
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the difference between the current date and the start date
    delta = current_date - start_date
    
    # Return the number of days passed
    return delta.days

# Example usage
start_date = '2023-01-01'  # Replace with your start date
days_passed = days_passed_since(start_date)
print(f"Days passed since {start_date}: {days_passed}")

def set_wallpaper():
    if os.path.exists('hs.jpg'):
        os.remove('hs.jpg')
    if os.path.exists('hs.html'):
        os.remove('hs.html')
    if os.path.exists('ls.jpg'):
        os.remove('ls.jpg')
    if os.path.exists('ls.html'):
        os.remove('ls.html')
    quotes=json.load(open('data/quotes.json','r'))
    hti=Html2Image()
    template_loader=jinja2.FileSystemLoader('./')
    template_env=jinja2.Environment(loader=template_loader)
    template=template_env.get_template('data/html/hs.html')
    templatels=template_env.get_template('data/html/ls.html')
    images_list=os.listdir('data/images')
    image_file=(base64.b64encode(open(os.path.abspath('data\\images\\'+images_list[random.randrange(0,len(images_list)-1)]),'rb').read())).decode('utf-8')
    data_=json.load(open('app_data.json','r'))
    


    x=open('hs.html','x')
    x.write(template.render({'quote':list(quotes.values())[random.randrange(0,len(quotes.keys())-1)],'days_to':days_left_until(data_['goal_date']),'days_passed':days_passed_since(data_['start_date']),'base64_string':image_file}))
    x.close()
    hti.screenshot(html_file='hs.html',save_as='hs.jpg')
    
    wallpaper_style = 0
    # Load the image
    SPI_SETDESKWALLPAPER = 20
    image = ctypes.c_wchar_p(os.path.abspath('hs.jpg'))
        # Set the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, wallpaper_style)
    # hti1=Html2Image()
    # y=open('ls.html','x')
    # y.write(templatels.render({'Days_Left':days_left_until(data_['goal_date']),'Days_Passed':days_passed_since(data_['start_date'])}))
    # y.close()
    # hti1.screenshot(html_file='ls.html',save_as='ls.jpg')

    # # SPI_SETDESKWALLPAPER = 20
    # SPIF_UPDATEINIFILE = 1
    # SPIF_SENDCHANGE = 2
    
    # # Load the user32 DLL
    # user32 = ctypes.windll.user32
    
    # # Change the lock screen wallpaper
    # result = user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath('ls.html'), SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)


def app_setup():
    def save_data():
        selected_date = date_entry.get_date()

        if not os.path.exists('app_data.json'):
            json_data={"goal_date":str(selected_date),"start_date":datetime.now().strftime('%Y-%m-%d'),'current_date':datetime.now().strftime('%Y-%m-%d')}
            z=open('app_data.json','x')
            z.write(json.dumps(json_data))
            z.close()
        



    # Create the main window
    root = tk.Tk()
    root.title("Wallpaper Day Counter")

    # Label
    label = tk.Label(root, text="Wallpaper Day Counter", font=("Arial", 14))
    label.pack(pady=10)

    # Date picker
    date_label = tk.Label(root, text="Select Goal Date:")
    date_label.pack(pady=5)
    date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
    date_entry.pack(pady=5)



    # Save button
    save_button = tk.Button(root, text="Save", command=save_data)
    save_button.pack(pady=20)

    # Run the application
    root.mainloop()
if not os.path.exists('app_data.json'):
    app_setup()
else:
    set_wallpaper()