package main

import (
	//"image/color"
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/driver/desktop"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
)
func main() {
	application := app.New()
	newWindow := application.NewWindow("Box Layout")
	
    newWindow.SetMainMenu(menuSetup())

    //create shortcuts
	arr := ShortCutSetup()    
	
	//instantiate shortcuts
	for _, element := range arr {	
		newWindow.Canvas().AddShortcut(element,func(shortcut fyne.Shortcut){
				newWindow.Close()
		})
	}

	input := widget.NewEntry()
	input.SetPlaceHolder("Enter text...")


	bottomCenter := container.New(layout.NewMaxLayout(), layout.NewSpacer(), input)

	newWindow.SetContent(container.New(layout.NewVBoxLayout(), bottomCenter))

	newWindow.Resize(fyne.NewSize(600,300))

	newWindow.ShowAndRun()
}

func ShortCutSetup() []*desktop.CustomShortcut {
	ctrlQ := &desktop.CustomShortcut{
    	KeyName: fyne.KeyQ, 
    	Modifier: fyne.KeyModifierControl,
    }

    return []*desktop.CustomShortcut{ctrlQ}
}

func menuSetup() *fyne.MainMenu {
	menuItem1 := fyne.NewMenuItem("New", nil)
    menuItem2 := fyne.NewMenuItem("Save", nil)
    menuItem3 := fyne.NewMenuItem("edit", nil)
    
    newMenu := fyne.NewMenu("File", menuItem1, menuItem2, menuItem3)
    
    menu := fyne.NewMainMenu(newMenu) 

    return menu
}