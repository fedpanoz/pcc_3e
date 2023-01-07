from Solution9_11_part import Admin

mio_admin = Admin('fedez', 'panoz', 'fedpanoz', 'fedpaoz@yahoo.it', 'borghetto')
mio_admin.describe_user()
supercazzola = ['accetta', 'banna', 'rifiuta']
# mio_admin.privileges.show_privileges()

mio_admin.privilegiazzo.privilegio = supercazzola

mio_admin.privilegiazzo.show_privileges()


