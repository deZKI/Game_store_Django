function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

const forms = document.querySelector('form[name=filter]');

forms.addEventListener('submit', function (e) {
    // Получаем данные из формы
    e.preventDefault();
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);
});

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.col-lg-9>.row');
    div.innerHTML = output;
}

let html = '\
{{#games}}\
      <div class="col-6 col-md-4 col-xl-3">\
                                <div class="product-default inner-quickview inner-icon">\
                                    <figure>\
                                        <a href="/catalog/game/{{slug}}">\
\
                                            <img src="http://127.0.0.1:8000/media/{{images__image }}">\
                                        </a>\
                                        <div class="btn-icon-group">\
                                            <button class="btn-icon btn-add-cart" data-toggle="modal"\
                                                    data-target="#addCartModal"><i class="icon-bag"></i></button>\
                                        </div>\
                                        <a href="{% static \'/ajax/product-quick-view.html\' %}" class="btn-quickview"\
                                           title="Quick View">Quick View</a>\
                                    </figure>\
                                    <div class="product-details">\
                                        <h2 class="product-title">\
                                            <a href="/catalog/game/{{slug}}">{{ name }}</a>\
                                        </h2>\
                                        <div class="ratings-container">\
                                            <div class="product-ratings">\
                                                <span class="ratings"\
                                                      style="width:100%"></span>\
                                                <!-- End .ratings -->\
                                                <span class="tooltiptext tooltip-top"></span>\
                                            </div><!-- End .product-ratings -->\
                                        </div><!-- End .product-container -->\
                                        <div class="price-box">\
                                            <span class="product-price">{{ price }}</span>\
                                        </div><!-- End .price-box -->\
                                    </div><!-- End .product-details -->\
                                </div>\
                            </div>\
{{/games}}'