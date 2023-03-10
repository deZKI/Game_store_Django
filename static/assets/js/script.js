const ajax_filter = document.querySelector('form[name=filter]')
let param_form = ''

function ajaxSend(url) {
    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json, url))
        .catch(error => console.error(error))
}

function ajaxPagination(press_value) {
    let url = this.form.action
    url = `${url}?${param_form}page=${press_value}`
    ajaxSend(url)
}

ajax_filter.addEventListener('submit', function (e) {
    // Получаем данные из формы
    e.preventDefault()
    let url = this.action
    params = new URLSearchParams(new FormData(this))
    param_form = ''

    let keys = new Set(params.keys())
    console.log(keys)
    console.log(params)
    for (const key of keys) {
        param_form = key + '=' + params.getAll(key).join(',') + '&' + param_form
    }
    url = `${url}?${param_form}`
    ajaxSend(url)
});

function render(data) {
    // Рендер шаблона
    const divgames = document.querySelector('.col-lg-9>.row')
    const divpagen = document.querySelector('.col-lg-9>.toolbox-pagination')

    if (data.games.length === 0) {
        divgames.innerHTML = '<h2>Игр нет, попробуйте поменять параметры поиска</h2>'
        divpagen.innerHTML = ''
    } else {
        let game_list_h = Hogan.compile(htmlGames)
        let game_list = game_list_h.render(data)
        divgames.innerHTML = game_list


    }
}

let htmlGames = '\
{{#games}}\
<div class="col-6 col-md-4 col-xl-3">\
                                <div class="product-default inner-quickview inner-icon">\
                                    <figure>\
                                        <a href="/catalog/game/{{slug}}">\
\
                                            <img src="{{main_image}}" style="height: 200px;width:200px">\
                                        </a>\
                                        <div class="btn-icon-group">\
                                            <button class="btn-icon btn-add-cart" data-toggle="modal"\
                                                    data-target="#addCartModal"><i class="icon-bag"></i></button>\
                                        </div>\
                                        <a href="/catalog/modal-game/{{slug}}" class="btn-quickview"\
                                           title="Quick View">Quick View</a>\
                                    </figure>\
                                    <div class="product-details">\
                                        <h2 class="product-title">\
                                            <a href="/catalog/game/{{slug}}">{{ name }}</a>\
                                        </h2>\
                                        <div class="price-box">\
                                            <span class="product-price">{{ price }}</span>\
                                        </div><!-- End .price-box -->\
                                    </div><!-- End .product-details -->\
                                </div>\
     </div>\
{{/games}}'

let htmlPagin = '<li class="page-item"  value="?page={{ page }}"><button class="page-link">{{ page }}</button></li>'
