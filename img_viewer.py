from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.attributes('-fullscreen', True)
root.title('Image Viewer')

# opening and appending the images to be displayed to a list
my_img1 = ImageTk.PhotoImage(Image.open("images/img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/img4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/img5.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


# creating the label to display the image and inserting it in the window
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


# function for forward button
def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget() # clearing the previous set image
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))
	
	if image_number == 5:
		# disabling the forward button at end of the list
		button_forward = Button(root, text=">>", state=DISABLED)

	# inserting the buttons in the window
	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)


# function for backward button
def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget() # clearing the previous set image
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 1:
		# disabling the backward button at beginning of the list
		button_back = Button(root, text="<<", state=DISABLED)

	# inserting the buttons in the window
	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)


# creating the buttons
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


# inserting the buttons in the window
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()