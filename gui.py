from tkinter import*
from weatherForecast import weather
from tkinter import messagebox


root=Tk()
root.title('Weather Forecast')
#define the entries
display_precipitation=Entry(root,width=35,bg="blue",fg="white",borderwidth=5)
display_max_temp=Entry(root,width=35,bg="blue",fg="white",borderwidth=5)
display_min_temp=Entry(root,width=35,bg="blue",fg="white",borderwidth=5)
display_wind=Entry(root,width=35,bg="blue",fg="white",borderwidth=5)
#define a label where predicted weather will be displayed
display_weather=Label(root,text="")
#define labels
label1=Label(root,text="Precipitation")
label2=Label(root,text="Maximum Temperature")
label3=Label(root,text="Minimum Temperature")
label4=Label(root,text="Wind")





def ok():
    try:
        precipitation=float(display_precipitation.get())
        max_temp=float(display_max_temp.get())
        min_temp=float(display_min_temp.get())
        wind=float(display_wind.get())
        weather(precipitation,max_temp,min_temp,wind)

        #Make predictions
        prediction=weather(precipitation,max_temp,min_temp,wind)

        #display predictions on label
        display_weather.config(text=f"predicted weather: {prediction[0]}")
        
    
    except ValueError:
        #displaying error in the label
        #display_weather.config(text="Error please enter valid numbers.")
        #showing messagebox error instead of displaying it in the label
        messagebox.showerror("Value Error!","Please enter valid numbers or check for missing fields")
    except  Exception as e:
        #displaying error in the label
        #display_weather.config(text=f"Error :{e}")
        messagebox.showerror("Error!",f"Error :{e}")



button_ok=Button(root,text="Ok",command=ok)
button_exit=Button(root,text="Exit",command=root.quit)

display_precipitation.grid(row=1,column=1)
display_max_temp.grid(row=2,column=1)
display_min_temp.grid(row=3,column=1)
display_wind.grid(row=4,column=1)
#display labels
label1.grid(row=1,column=0)
label2.grid(row=2,column=0)
label3.grid(row=3,column=0)
label4.grid(row=4,column=0)
display_weather.grid(row=0,column=0,columnspan=3)
#display exit and ok button
button_ok.grid(row=5,column=0)
button_exit.grid(row=5,column=2)

root.mainloop()

