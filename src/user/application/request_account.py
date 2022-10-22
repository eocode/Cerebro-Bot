from src.room.application.use_case.get_room import GetRoom
from src.user.application.use_case.get_account import GetAccount


def request_account(user):
    usr, access, info = GetAccount().execute(permission='settings', chat_id=user.id,
                                             name=user.first_name, username=user.username)

    response = [f"🧠 Nombre: {info.full_name}\n📱 Telefono: {info.phone}\nActivo: {'🟢' if info.verify else '🔴'}"]

    if access:
        response.append(
            f"🏡 Hospedado en {info.room_name.lower()}\nDesde el {info.room_start_date}\n{f'Hasta el {info.room_end_date}' if info.room_end_date is not None else ''}")
        response.append(
            f"Consulta más acciones en /ayuda")

    return response
