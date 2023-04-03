from swagger_server.models.response_institution import ResponseInstitution
from swagger_server.models.response_institution_data import ResponseInstitutionData


class InstitutionUseCase:

    def __init__(self, institution_repository):
        self.institution_repository = institution_repository

    def get_institution(self):
        """
            Proceso instutition
        :return:
        """

        data_response = []
        institutions = self.institution_repository.get_institution()

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address,
                )
            )

        response = ResponseInstitution(
            code=0,
            message="Proceso Aceptado",
            data=data_response
        )

        return response

    def delete_institution(self, institution_id):
        """
        Proceso de Eliminacion de una institucion
        :return:
        """
        rows_affected = self.institution_repository.delete_institution(institution_id)
        if rows_affected > 0:
            response = ResponseInstitution(code=200, message="Proceso Aceptado")
        else:
            response = ResponseInstitution(code=-1, message="No se pudo Eliminar")

        return response