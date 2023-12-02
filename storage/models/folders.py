
class Folder(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    created_at = models.DateTimeField(default=datetime.now, verbose_name='Дата создания')
    name = models.CharField(max_length=255, verbose_name='Папка')
    parent_id = models.IntegerField(verbose_name='Родительский каталог', blank=True, null=True)
    # url = models.SlugField(max_length=160, unique=True)
    # files = models.ManyToManyField(File, verbose_name='Файлы', related_name='folders', through='FileScope')

    class Meta:
        verbose_name = 'Папка'
        verbose_name_plural = 'Папки'
        ordering = ['name']

    def __str__(self):
        return self.name
