// Convert vanilla Javascript to JQuery

// Ready function for JQuery
$(() => {
    // Selecting the Header
    const headerDiv = $('div:first')

    // Changing the Background
    const changeBackground = (color) => {
        headerDiv.css('background-color', color)
    }

    // Event Listeners for the Header
    headerDiv.mouseenter(() => {
        changeBackground("pink")
    }).mouseleave(() => {
        changeBackground("red")
    }).click(() => {
        alert("Hello From the First Div")
    })

    // Functionality for the Color Picker
    $('#favcolor').change(() => {
        changeBackground($('#favcolor').val())
    })

    // Creating the Comment Section
    const scrollDiv = $('<div></div>').attr('id', 'scrollDiv').css('background-color', 'yellow')
    $('main').append(scrollDiv)

    // Creating the Scroll Count
    const scrollDisplay = $('<h3></h3>').attr('id', 'scrollDisplay').html('<span>Scroll Count: </span><span id="counter">0</span>')
    scrollDiv.append(scrollDisplay)

    // Functionality for the Scroll Counter
    const scrollCount = () => {
        $('span#counter').text((i, old) => {
            old++
            return old
        })
    }

    // Event Listener for the Scroll Counter
    scrollDiv.click(() => {
        scrollCount()
    })

    // Function for creating a fake comment
    const commentFunc = () => {
        const ptag = $('<p></p>').text("In magna migas chillwave, lo-fi banh mi bitters consectetur labore. DIY franzen velit offal vexillologist. Brunch yuccie mixtape, meggings sustainable ea jean shorts af iceland minim. Tousled snackwave vexillologist excepteur semiotics bushwick. XOXO minim seitan tbh adaptogen air plant mustache bicycle rights poke duis readymade yuccie magna iceland.")
        scrollDiv.append(ptag)
    }

    // Starting with 4 comments
    for (let index = 0; index < 4; index++) {
        commentFunc()
    }

    // Cehcking the scroll position to update the Comment Section
    const scrollCheck = () => {
        if (window.pageYOffset >= document.body.offsetHeight - window.innerHeight) {
            commentFunc()
        }
    }

    // Scroll Event for the window object to capture all the scrolls
    $(window).scroll(() => {
        scrollCheck()
        scrollCount()
    })
})