# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arl(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'arl'


class Barrio(models.Model):
    nombre = models.TextField()
    codigo = models.CharField(max_length=20, blank=True, null=True)
    codigo_comuna = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barrio'


class Cesantias(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cesantias'


class Comuna(models.Model):
    nombre = models.TextField()
    codigo = models.IntegerField(blank=True, null=True)
    prioriza = models.CharField(max_length=20, blank=True, null=True)
    prioriza2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'


class Demograficos(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    apellidos = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    cedula = models.IntegerField()
    correopersonal = models.CharField(db_column='correoPersonal', max_length=255, db_collation='latin1_swedish_ci')  # Field name made lowercase.
    genero = models.CharField(max_length=25, db_collation='latin1_swedish_ci')
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    direccion = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    estrato = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    telefono = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    tipovivienda = models.CharField(db_column='tipoVivienda', max_length=50, db_collation='latin1_swedish_ci')  # Field name made lowercase.
    estadocivil = models.CharField(db_column='estadoCivil', max_length=50, db_collation='latin1_swedish_ci')  # Field name made lowercase.
    nivelformacion = models.CharField(db_column='nivelFormacion', max_length=50, db_collation='latin1_swedish_ci')  # Field name made lowercase.
    tituloobtenido = models.CharField(db_column='tituloObtenido', max_length=50, db_collation='latin1_swedish_ci')  # Field name made lowercase.
    nombreconyuge = models.CharField(db_column='nombreConyuge', max_length=50, db_collation='latin1_swedish_ci')  # Field name made lowercase.
    condicionespecial = models.CharField(db_column='condicionEspecial', max_length=8, db_collation='latin1_swedish_ci')  # Field name made lowercase.
    departamentonaci = models.CharField(db_column='departamentoNaci', max_length=100)  # Field name made lowercase.
    departamentoresi = models.CharField(db_column='departamentoResi', max_length=100)  # Field name made lowercase.
    paisnaci = models.CharField(db_column='paisNaci', max_length=30)  # Field name made lowercase.
    municipioresi = models.CharField(db_column='municipioResi', max_length=30)  # Field name made lowercase.
    municipionaci = models.CharField(db_column='municipioNaci', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'demograficos'


class Departamento(models.Model):
    nombre = models.TextField()
    codigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class Discapacidades(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'discapacidades'


class Empleabilidad(models.Model):
    id_empleabilidad = models.AutoField(primary_key=True)
    id_empleado = models.IntegerField()
    correoinstitucional = models.CharField(db_column='correoInstitucional', max_length=50)  # Field name made lowercase.
    eps = models.CharField(max_length=50)
    fondopension = models.CharField(db_column='fondoPension', max_length=50)  # Field name made lowercase.
    cesantias = models.CharField(max_length=50)
    arl = models.CharField(max_length=50)
    nivelriesgo = models.CharField(db_column='nivelRiesgo', max_length=50)  # Field name made lowercase.
    objeto = models.CharField(max_length=50)
    valormensual = models.CharField(db_column='valorMensual', max_length=50)  # Field name made lowercase.
    fechainicio = models.DateField(db_column='fechaInicio')  # Field name made lowercase.
    fechaterminacion = models.DateField(db_column='fechaTerminacion')  # Field name made lowercase.
    valorcontrato = models.CharField(db_column='valorContrato', max_length=50)  # Field name made lowercase.
    supervisor = models.CharField(max_length=50)
    carnet = models.CharField(max_length=50)
    numeropoliza = models.CharField(db_column='numeroPoliza', max_length=50)  # Field name made lowercase.
    nuevos = models.CharField(max_length=50)
    estadoempleado = models.CharField(db_column='estadoEmpleado', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleabilidad'


class Eps(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'eps'


class FondosPensiones(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'fondos_pensiones'


class Hijos(models.Model):
    id_hijo = models.AutoField(primary_key=True)
    id_empleado = models.IntegerField()
    nombres = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    apellidos = models.CharField(max_length=50, db_collation='latin1_swedish_ci')
    fechanacimiento = models.CharField(db_column='fechaNacimiento', max_length=50, db_collation='latin1_swedish_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hijos'


class Municipio(models.Model):
    nombre = models.TextField()
    codigo = models.IntegerField(blank=True, null=True)
    codigo_departamento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipio'


class Pais(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'pais'


class SituacionesAdministrativas(models.Model):
    id_situaciones = models.AutoField(primary_key=True)
    id_empleado = models.IntegerField()
    licencias = models.CharField(max_length=100)
    permisos = models.CharField(max_length=100)
    comision = models.TextField()
    encargo = models.CharField(max_length=100)
    suspencionejercicio = models.CharField(db_column='suspencionEjercicio', max_length=100)  # Field name made lowercase.
    periodoprueba = models.CharField(db_column='periodoPrueba', max_length=8)  # Field name made lowercase.
    vacaciones = models.CharField(max_length=100)
    otros = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'situaciones_administrativas'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    correo = models.CharField(max_length=30)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios'
