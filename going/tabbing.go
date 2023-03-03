import "fyne.io/fyne/v2"

func main() {
    // Create a new application window
    app := fyne.NewApp()
    win := app.NewWindow("My App")

    // Create a tab container with tabs on the left
    tabContainer := fyne.NewContainerWithLayout(
        fyne.NewHBoxLayout(),
        createTabBar(),
        createContentArea(),
    )

    // Set the tab container as the window content
    win.SetContent(tabContainer)

    // Show the window
    win.ShowAndRun()
}

func createTabBar() fyne.CanvasObject {
    // Create a tab bar with some example tabs
    tabItems := []*fyne.Container{
        fyne.NewContainerWithLayout(
            fyne.NewHBoxLayout(),
            fyne.NewLabel("Tab 1"),
        ),
        fyne.NewContainerWithLayout(
            fyne.NewHBoxLayout(),
            fyne.NewLabel("Tab 2"),
        ),
        fyne.NewContainerWithLayout(
            fyne.NewHBoxLayout(),
            fyne.NewLabel("Tab 3"),
        ),
    }
    tabBar := fyne.NewContainerWithLayout(
        fyne.NewVBoxLayout(),
        tabItems...,
    )
    return tabBar
}

    func createContentArea() fyne.CanvasObject {
    // Create a content area with some example content
    content := fyne.NewContainerWithLayout(
        fyne.NewVBoxLayout(),
        fyne.NewLabel("Content area"),
    )
    return content
}
