import tkinter as tk
import UpperBodyModule as ubm
import LowerBodyModule as lbm

def train_upperbody():
    """
    Initiates an upper body training routine with a preset parameter.
    
    Calls the upperBody function from the UpperBodyModule with px set to 3.
    """
    ubm.upperBody(px=3)
    
def train_lowerbody():
    """
    Triggers the lower body training routine by invoking the lowerBody function from the LowerBodyModule.
    """
    lbm.lowerBody()

root = tk.Tk()
root.title("Body Training App")

label = tk.Label(root, text="Choose which body part you want to train:")
label.pack()

upperbody_button = tk.Button(root, text="Train Upper Body", command=train_upperbody)
upperbody_button.pack(pady=10)

lowerbody_button = tk.Button(root, text="Train Lower Body", command=train_lowerbody)
lowerbody_button.pack(pady=10)

root.mainloop()
