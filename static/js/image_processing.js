function change_image_pixel_colors(form, image) {
    let red_color = parseInt(form.elements["red_color_control"].value);
    let blue_color = form.elements["blue_color_control"].value;
    let green_color = form.elements["green_color_control"].value;
    let canvas = document.getElementById('myCanvas');
    let context = canvas.getContext('2d');
    let img = image;
    canvas.width = img.width;
    canvas.height = img.height;
    context.drawImage(img, 0, 0 );
    let img_data = context.getImageData(0, 0, img.width, img.height);
    for (let i =0; i < img_data.data.length; i +=4)
    {
        img_data.data[i] += red_color - 50;
        img_data.data[i+1] += green_color - 50;
        img_data.data[i+2] += blue_color - 50;
    }
    context.putImageData(img_data, 0, 0);
    context.stroke();
}
function load_image(image) {
    let canvas = document.getElementById('myCanvas');
    let context = canvas.getContext('2d');
    let img = image;
    canvas.width = img.width;
    canvas.height = img.height;
    context.drawImage(img, 0, 0 );
    canvas.width = img.width;
    canvas.height = img.height;
    context.drawImage(img, 0, 0 );
    context.stroke();
}
