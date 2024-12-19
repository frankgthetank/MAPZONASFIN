let selectedIds = [];  // Lista para almacenar los IDs seleccionados

// Esta función se ejecuta cuando un elemento del mapa es clickeado
function handle_click(e, feature) {
    const id = feature.properties.id;  // Obtener el ID del elemento

    // Añadir el ID a la lista si no está ya en ella
    if (!selectedIds.includes(id)) {
        selectedIds.push(id);
        console.log(`ID ${id} añadido a la lista`);
    } else {
        console.log(`ID ${id} ya está en la lista`);
    }

    // Enviar los IDs seleccionados al servidor para actualizar el archivo .gpkg
    fetch('/update_ids', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            selected_ids: selectedIds
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);  // Mensaje de éxito
    })
    .catch(error => {
        console.error('Error al actualizar los IDs:', error);
    });
}
