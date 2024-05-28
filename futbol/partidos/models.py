from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    def puntos(self):
        puntos_local = sum(partido.goles_local if partido.equipo_local == self else 0 for partido in self.partidos_local.all())
        puntos_visitante = sum(partido.goles_visitante if partido.equipo_visitante == self else 0 for partido in self.partidos_visitante.all())
        return (puntos_local + puntos_visitante) or 0
    def partidos_jugados(self):
        return self.partidos_local.count() + self.partidos_visitante.count()

    def partidos_ganados(self):
        ganados_local = self.partidos_local.filter(goles_local__gt=models.F('goles_visitante')).count()
        ganados_visitante = self.partidos_visitante.filter(goles_visitante__gt=models.F('goles_local')).count()
        return ganados_local + ganados_visitante

    def partidos_empatados(self):
        empatados_local = self.partidos_local.filter(goles_local=models.F('goles_visitante')).count()
        empatados_visitante = self.partidos_visitante.filter(goles_local=models.F('goles_visitante')).count()
        return empatados_local + empatados_visitante

    def partidos_perdidos(self):
        perdidos_local = self.partidos_local.filter(goles_local__lt=models.F('goles_visitante')).count()
        perdidos_visitante = self.partidos_visitante.filter(goles_visitante__lt=models.F('goles_local')).count()
        return perdidos_local + perdidos_visitante

    def goles_a_favor(self):
        goles_local = self.partidos_local.aggregate(models.Sum('goles_local'))['goles_local__sum'] or 0
        goles_visitante = self.partidos_visitante.aggregate(models.Sum('goles_visitante'))['goles_visitante__sum'] or 0
        return goles_local + goles_visitante

    def goles_en_contra(self):
        goles_recibidos_local = self.partidos_local.aggregate(models.Sum('goles_visitante'))['goles_visitante__sum'] or 0
        goles_recibidos_visitante = self.partidos_visitante.aggregate(models.Sum('goles_local'))['goles_local__sum'] or 0
        return goles_recibidos_local + goles_recibidos_visitante

class Partido(models.Model):
    equipo_local = models.ForeignKey(Equipo, related_name='partidos_local', on_delete=models.CASCADE)
    equipo_visitante = models.ForeignKey(Equipo, related_name='partidos_visitante', on_delete=models.CASCADE)
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()

    def __str__(self):
        return f'{self.equipo_local} vs {self.equipo_visitante}'
