// static/main.js

const API_BASE = ""; // mismo dominio: http://127.0.0.1:8000

const form = document.getElementById("form-pedido");
const tablaPedidos = document.getElementById("tabla-pedidos");

// --------- Función para cargar todos los pedidos ---------
async function cargarPedidos() {
  try {
    const res = await fetch(`${API_BASE}/pedidos/`);
    if (!res.ok) {
      console.error("Error al obtener pedidos");
      return;
    }
    const pedidos = await res.json();
    renderPedidos(pedidos);
  } catch (error) {
    console.error("Error de red al obtener pedidos", error);
  }
}

// --------- Pintar pedidos en la tabla ---------
function renderPedidos(pedidos) {
  tablaPedidos.innerHTML = "";

  if (!pedidos || pedidos.length === 0) {
    const fila = document.createElement("tr");
    const celda = document.createElement("td");
    celda.colSpan = 6;
    celda.textContent = "No hay pedidos registrados";
    fila.appendChild(celda);
    tablaPedidos.appendChild(fila);
    return;
  }

  pedidos.forEach((p) => {
    const tr = document.createElement("tr");

    const tdId = document.createElement("td");
    tdId.textContent = p.id;

    const tdCliente = document.createElement("td");
    tdCliente.textContent = p.cliente;

    const tdProducto = document.createElement("td");
    tdProducto.textContent = p.producto;

    const tdFecha = document.createElement("td");
    tdFecha.textContent = p.fecha_entrega;

    const tdEstado = document.createElement("td");
    const spanEstado = document.createElement("span");
    spanEstado.textContent = p.estado;
    spanEstado.classList.add("estado-pill");
    tdEstado.appendChild(spanEstado);

    const tdAcciones = document.createElement("td");

    const estados = [
      "pendiente",
      "en_preparacion",
      "entregado",
      "cancelado",
    ];

    estados.forEach((estado) => {
      const btn = document.createElement("button");
      btn.textContent = estado.replace("_", " ");
      btn.style.marginRight = "4px";
      btn.onclick = () => cambiarEstadoPedido(p.id, estado);
      tdAcciones.appendChild(btn);
    });

    tr.appendChild(tdId);
    tr.appendChild(tdCliente);
    tr.appendChild(tdProducto);
    tr.appendChild(tdFecha);
    tr.appendChild(tdEstado);
    tr.appendChild(tdAcciones);

    tablaPedidos.appendChild(tr);
  });
}

// --------- Cambiar estado de un pedido ---------
async function cambiarEstadoPedido(id, nuevoEstado) {
  try {
    const res = await fetch(
      `${API_BASE}/pedidos/${id}/estado?nuevo_estado=${nuevoEstado}`,
      {
        method: "PUT",
      }
    );

    if (!res.ok) {
      console.error("Error al cambiar estado del pedido");
      return;
    }

    await cargarPedidos();
  } catch (error) {
    console.error("Error de red al cambiar estado", error);
  }
}

// --------- Manejo del formulario de nuevo pedido ---------
form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const cliente = document.getElementById("cliente").value.trim();
  const telefono = document.getElementById("telefono").value.trim();
  const producto = document.getElementById("producto").value.trim();
  const sabor = document.getElementById("sabor").value.trim();
  const tamano = document.getElementById("tamano").value.trim();
  const precio = parseFloat(document.getElementById("precio").value);
  const fecha_entrega = document.getElementById("fecha_entrega").value;
  const estado = document.getElementById("estado").value;

  if (!fecha_entrega) {
    alert("Debes seleccionar una fecha de entrega");
    return;
  }

  const payload = {
    cliente_id: null,      // opcional por ahora
    producto_id: null,     // opcional por ahora
    cliente,
    telefono,
    producto,
    sabor,
    tamano,
    precio,
    fecha_entrega,
    estado,
  };

  try {
    const res = await fetch(`${API_BASE}/pedidos/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!res.ok) {
      console.error("Error al crear pedido");
      alert("No se pudo crear el pedido");
      return;
    }

    form.reset();
    await cargarPedidos();
  } catch (error) {
    console.error("Error de red al crear pedido", error);
  }
});

// --------- Cuando carga la página, traemos los pedidos ---------
document.addEventListener("DOMContentLoaded", () => {
  cargarPedidos();
});
