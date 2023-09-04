describe("Pruebas de la PetStore API", () => {
  it("Crear un usuario, buscarlo, actualizarlo y eliminarlo", () => {
    // Paso 1: Crear un usuario
    cy.request({
      method: "POST",
      url: "https://petstore.swagger.io/v2/user",
      body: {
        id: 0,
        username: "marcialito",
        firstName: "nombre",
        lastName: "apellido",
        email: "correo@example.com",
        password: "contraseña",
        phone: "123456789",
        userStatus: 0,
      },
    }).then((response) => {
      expect(response.status).to.eq(200); // Verifica que la creación del usuario sea exitosa

      // Paso 2: Buscar el usuario creado
      cy.request({
        method: "GET",
        url: "https://petstore.swagger.io/v2/user/marcialito", // Reemplaza 'nombre_de_usuario' con el nombre de usuario creado
      }).then((response) => {
        expect(response.status).to.eq(200); // Verifica que la búsqueda del usuario sea exitosa

        // Paso 3: Actualizar el nombre y el correo del usuario
        cy.request({
          method: "PUT",
          url: "https://petstore.swagger.io/v2/user/marcialito", // Reemplaza 'nombre_de_usuario' con el nombre de usuario creado
          body: {
            id: 0,
            username: "marcialito",
            firstName: "nuevo_nombre",
            lastName: "apellido",
            email: "nuevo_correo@example.com",
            password: "contraseña",
            phone: "123456789",
            userStatus: 0,
          },
        }).then((response) => {
          expect(response.status).to.eq(200); // Verifica que la actualización sea exitosa

          // Paso 4: Buscar el usuario actualizado
          cy.request({
            method: "GET",
            url: "https://petstore.swagger.io/v2/user/marcialito", // Reemplaza 'nombre_de_usuario' con el nombre de usuario creado
          }).then((response) => {
            expect(response.status).to.eq(200); // Verifica que la búsqueda del usuario actualizado sea exitosa

            // Paso 5: Eliminar el usuario
            cy.request({
              method: "DELETE",
              url: "https://petstore.swagger.io/v2/user/marcialito", // Reemplaza 'nombre_de_usuario' con el nombre de usuario creado
            }).then((response) => {
              expect(response.status).to.eq(200); // Verifica que la eliminación sea exitosa
            });
          });
        });
      });
    });
  });
});
