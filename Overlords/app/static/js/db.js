const API_SERVER = 'http://127.0.0.1:8000';

// Función para realizar la petición fetch
async function fetchData(url, method, data = null) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: data ? JSON.stringify(data) : null,
    };

    const response = await fetch(url, options);
    return await response.json();
}

async function fetchDataWithFile(url, method, formData) {
    const options = {
        method: method,
        body: formData,
    };

    const response = await fetch(url, options);
    return await response.json();
}

// Agrega usuarios a la base de datos.
document.getElementById('btn-add-data').addEventListener('click', async function () {
    const id_user = document.querySelector('#id_user');
    const name   = document.querySelector('#name').value;
    const mail = document.querySelector('#mail').value;
    const password = document.querySelector('#password').value;

    const formData = new FormData();
    formData.append('name', name);
    formData.append('mail', mail);
    formData.append('password', password);
    let result = null;
    if(id_user.value!==""){
      result = await fetchDataWithFile(`${API_SERVER}/edit_data/${id_user.value}/`, 'POST', formData);
    }else{
      result = await fetchDataWithFile(`${API_SERVER}/add_data/`, 'POST', formData);
    }
    const dataPanel = document.querySelector('#data_panel');
    id_user.value=''
    dataPanel.reset();
    alert(result.message);

    viewDataUser();
});

// Muestra las llamadas a la base de datos en el HTML.
  async function viewDataUser(){
    let user =  await fetchData(API_SERVER+'/get_data/', 'GET');
    const tableUser = document.querySelector('#userList tbody');
    tableUser.innerHTML='';
    user.forEach((user, index) => {
      let tr = `<tr>
                    <td>${user.name}</td>
                    <td>${user.mail}</td>
                    <td>${user.password}</td>
                    <td>
                        <button class="btn btn-info" onclick='userUpdate(${user.id})'><i class="btn btn-info" ></button></i>
                        <button class="btn btn-danger" onclick='delUser(${user.id})'><i class="btn btn-danger" ></button></i>
                    </td>
                  </tr>`;
      tableUser.insertAdjacentHTML("beforeend",tr);
    });
  }
  
  // Elimina el registro indicado.
  async function delUser(id){
    let response = await fetchData(`${API_SERVER}/del_data/${id}/`, 'DELETE');
    console.log(response);
    viewDataUser();
  }

// Edita el registro indicado.
  async function userUpdate(id){
    let response = await fetchData(`${API_SERVER}/edit_data/${id}/`, 'GET');
    const id_user = document.querySelector('#id_user');
    const name = document.querySelector('#name');
    const mail = document.querySelector('#mail');
    const password = document.querySelector('#password');
    
    id_user.value = response.id;
    name.value = response.name;
    mail.value = response.mail;
    password.value = response.password;
  }

  viewDataUser();