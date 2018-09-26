# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tblbonusset(models.Model):
    set = models.PositiveIntegerField(primary_key=True)
    tagid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'tblBonusSet'
        unique_together = (('set', 'tagid'),)


class Tblbuilding(models.Model):
    region = models.CharField(primary_key=True, max_length=2)
    when = models.DateTimeField()
    id = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    next = models.DateTimeField(blank=True, null=True)
    contributed = models.FloatField(blank=True, null=True)
    buff1 = models.PositiveIntegerField(blank=True, null=True)
    buff2 = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblBuilding'
        unique_together = (('region', 'when', 'id'),)


class Tbldbccurvepoint(models.Model):
    curve = models.PositiveSmallIntegerField(primary_key=True)
    step = models.PositiveIntegerField()
    key = models.FloatField()
    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tblDBCCurvePoint'
        unique_together = (('curve', 'step'),)


class Tbldbcenchants(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    effect = models.CharField(max_length=64, blank=True, null=True)
    gem = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblDBCEnchants'


class Tbldbcitem(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(
        max_length=250,
        db_column='name_enus',
        default=''
    )
    name_dede = models.CharField(max_length=250, blank=True, null=True)
    name_eses = models.CharField(max_length=250, blank=True, null=True)
    name_frfr = models.CharField(max_length=250, blank=True, null=True)
    name_itit = models.CharField(max_length=250, blank=True, null=True)
    name_ptbr = models.CharField(max_length=250, blank=True, null=True)
    name_ruru = models.CharField(max_length=250, blank=True, null=True)
    quality = models.PositiveIntegerField()
    level = models.PositiveSmallIntegerField(blank=True, null=True)
    class_field = models.PositiveIntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    subclass = models.PositiveIntegerField()
    icon = models.CharField(max_length=120)
    stacksize = models.PositiveSmallIntegerField(blank=True, null=True)
    binds = models.PositiveIntegerField(blank=True, null=True)
    buyfromvendor = models.PositiveIntegerField(blank=True, null=True)
    selltovendor = models.PositiveIntegerField(blank=True, null=True)
    auctionable = models.PositiveIntegerField(blank=True, null=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    requiredlevel = models.PositiveIntegerField(blank=True, null=True)
    requiredskill = models.PositiveSmallIntegerField(blank=True, null=True)
    display = models.PositiveIntegerField(blank=True, null=True)
    flags = models.CharField(max_length=22)

    class Meta:
        managed = False
        db_table = 'tblDBCItem'


class Tbldbcitembonus(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    quality = models.PositiveIntegerField(blank=True, null=True)
    level = models.SmallIntegerField(blank=True, null=True)
    previewlevel = models.PositiveSmallIntegerField(blank=True, null=True)
    levelcurve = models.PositiveSmallIntegerField(blank=True, null=True)
    tagid = models.PositiveIntegerField(blank=True, null=True)
    tagpriority = models.PositiveIntegerField(blank=True, null=True)
    nameid = models.PositiveIntegerField(blank=True, null=True)
    namepriority = models.PositiveIntegerField(blank=True, null=True)
    socketmask = models.TextField(blank=True, null=True)  # This field type is a guess.
    statmask = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'tblDBCItemBonus'


class Tbldbcitemnamedescription(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    desc_enus = models.CharField(max_length=120, blank=True, null=True)
    desc_dede = models.CharField(max_length=120, blank=True, null=True)
    desc_eses = models.CharField(max_length=120, blank=True, null=True)
    desc_frfr = models.CharField(max_length=120, blank=True, null=True)
    desc_itit = models.CharField(max_length=120, blank=True, null=True)
    desc_ptbr = models.CharField(max_length=120, blank=True, null=True)
    desc_ruru = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblDBCItemNameDescription'


class Tbldbcitemrandomsuffix(models.Model):
    locale = models.CharField(primary_key=True, max_length=4)
    suffix = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'tblDBCItemRandomSuffix'
        unique_together = (('locale', 'suffix'),)


class Tbldbcitemreagents(models.Model):
    item = models.PositiveIntegerField()
    skillline = models.PositiveSmallIntegerField()
    reagent = models.PositiveIntegerField()
    quantity = models.DecimalField(max_digits=8, decimal_places=4)
    spell = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblDBCItemReagents'


class Tbldbcitemspell(models.Model):
    item = models.PositiveIntegerField(primary_key=True)
    spell = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'tblDBCItemSpell'
        unique_together = (('item', 'spell'),)


class Tbldbcitemsubclass(models.Model):
    class_field = models.PositiveIntegerField(db_column='class', primary_key=True)  # Field renamed because it was a Python reserved word.
    subclass = models.PositiveIntegerField()
    name_enus = models.CharField(max_length=250)
    name_dede = models.CharField(max_length=250, blank=True, null=True)
    name_eses = models.CharField(max_length=250, blank=True, null=True)
    name_frfr = models.CharField(max_length=250, blank=True, null=True)
    name_itit = models.CharField(max_length=250, blank=True, null=True)
    name_ptbr = models.CharField(max_length=250, blank=True, null=True)
    name_ruru = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblDBCItemSubClass'
        unique_together = (('class_field', 'subclass'),)


class Tbldbcitemvendorcost(models.Model):
    item = models.PositiveIntegerField(primary_key=True)
    copper = models.PositiveIntegerField(blank=True, null=True)
    npc = models.PositiveIntegerField(blank=True, null=True)
    npccount = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblDBCItemVendorCost'


class Tbldbcpet(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name_enus = models.CharField(max_length=250)
    name_dede = models.CharField(max_length=250, blank=True, null=True)
    name_eses = models.CharField(max_length=250, blank=True, null=True)
    name_frfr = models.CharField(max_length=250, blank=True, null=True)
    name_itit = models.CharField(max_length=250, blank=True, null=True)
    name_ptbr = models.CharField(max_length=250, blank=True, null=True)
    name_ruru = models.CharField(max_length=250, blank=True, null=True)
    type = models.PositiveIntegerField()
    icon = models.CharField(max_length=120)
    npc = models.PositiveIntegerField(blank=True, null=True)
    category = models.PositiveIntegerField(blank=True, null=True)
    flags = models.PositiveIntegerField(blank=True, null=True)
    power = models.SmallIntegerField(blank=True, null=True)
    stamina = models.SmallIntegerField(blank=True, null=True)
    speed = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblDBCPet'


class Tbldbcrandenchants(models.Model):
    id = models.IntegerField(primary_key=True)
    name_enus = models.CharField(max_length=64)
    name_dede = models.CharField(max_length=64, blank=True, null=True)
    name_eses = models.CharField(max_length=64, blank=True, null=True)
    name_frfr = models.CharField(max_length=64, blank=True, null=True)
    name_itit = models.CharField(max_length=64, blank=True, null=True)
    name_ptbr = models.CharField(max_length=64, blank=True, null=True)
    name_ruru = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblDBCRandEnchants'


class Tbldbcskilllines(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tblDBCSkillLines'


class Tbldbcspell(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    cooldown = models.PositiveIntegerField()
    skillline = models.PositiveSmallIntegerField(blank=True, null=True)
    qtymade = models.DecimalField(max_digits=7, decimal_places=2)
    crafteditem = models.PositiveIntegerField(blank=True, null=True)
    expansion = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblDBCSpell'


class Tblhousecheck(models.Model):
    house = models.PositiveSmallIntegerField(primary_key=True)
    nextcheck = models.DateTimeField(blank=True, null=True)
    lastdaily = models.DateField(blank=True, null=True)
    lastcheck = models.DateTimeField(blank=True, null=True)
    lastcheckresult = models.TextField(blank=True, null=True)
    lastchecksuccess = models.DateTimeField(blank=True, null=True)
    lastchecksuccessresult = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblHouseCheck'


class Tblitembonusesseen(models.Model):
    item = models.PositiveIntegerField(primary_key=True)
    bonus1 = models.PositiveSmallIntegerField()
    bonus2 = models.PositiveSmallIntegerField()
    bonus3 = models.PositiveSmallIntegerField()
    bonus4 = models.PositiveSmallIntegerField()
    observed = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'tblItemBonusesSeen'
        unique_together = (('item', 'bonus1', 'bonus2', 'bonus3', 'bonus4'),)


class Tblitemglobal(models.Model):
    item = models.PositiveIntegerField(primary_key=True)
    level = models.PositiveSmallIntegerField()
    region = models.CharField(max_length=2)
    median = models.DecimalField(max_digits=11, decimal_places=0)
    mean = models.DecimalField(max_digits=11, decimal_places=0)
    stddev = models.DecimalField(max_digits=11, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'tblItemGlobal'
        unique_together = (('item', 'level', 'region'),)


class Tblitemhistorydaily(models.Model):
    item = models.PositiveIntegerField()
    house = models.PositiveSmallIntegerField(primary_key=True)
    when = models.DateField()
    pricemin = models.PositiveIntegerField()
    priceavg = models.PositiveIntegerField()
    pricemax = models.PositiveIntegerField()
    pricestart = models.PositiveIntegerField()
    priceend = models.PositiveIntegerField()
    quantitymin = models.PositiveIntegerField()
    quantityavg = models.PositiveIntegerField()
    quantitymax = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'tblItemHistoryDaily'
        unique_together = (('house', 'item', 'when'),)


class Tblitemhistorymonthly(models.Model):
    item = models.PositiveIntegerField(primary_key=True)
    house = models.PositiveSmallIntegerField()
    level = models.PositiveSmallIntegerField()
    month = models.PositiveIntegerField()
    mktslvr01 = models.PositiveIntegerField(blank=True, null=True)
    qty01 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr02 = models.PositiveIntegerField(blank=True, null=True)
    qty02 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr03 = models.PositiveIntegerField(blank=True, null=True)
    qty03 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr04 = models.PositiveIntegerField(blank=True, null=True)
    qty04 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr05 = models.PositiveIntegerField(blank=True, null=True)
    qty05 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr06 = models.PositiveIntegerField(blank=True, null=True)
    qty06 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr07 = models.PositiveIntegerField(blank=True, null=True)
    qty07 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr08 = models.PositiveIntegerField(blank=True, null=True)
    qty08 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr09 = models.PositiveIntegerField(blank=True, null=True)
    qty09 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr10 = models.PositiveIntegerField(blank=True, null=True)
    qty10 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr11 = models.PositiveIntegerField(blank=True, null=True)
    qty11 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr12 = models.PositiveIntegerField(blank=True, null=True)
    qty12 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr13 = models.PositiveIntegerField(blank=True, null=True)
    qty13 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr14 = models.PositiveIntegerField(blank=True, null=True)
    qty14 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr15 = models.PositiveIntegerField(blank=True, null=True)
    qty15 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr16 = models.PositiveIntegerField(blank=True, null=True)
    qty16 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr17 = models.PositiveIntegerField(blank=True, null=True)
    qty17 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr18 = models.PositiveIntegerField(blank=True, null=True)
    qty18 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr19 = models.PositiveIntegerField(blank=True, null=True)
    qty19 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr20 = models.PositiveIntegerField(blank=True, null=True)
    qty20 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr21 = models.PositiveIntegerField(blank=True, null=True)
    qty21 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr22 = models.PositiveIntegerField(blank=True, null=True)
    qty22 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr23 = models.PositiveIntegerField(blank=True, null=True)
    qty23 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr24 = models.PositiveIntegerField(blank=True, null=True)
    qty24 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr25 = models.PositiveIntegerField(blank=True, null=True)
    qty25 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr26 = models.PositiveIntegerField(blank=True, null=True)
    qty26 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr27 = models.PositiveIntegerField(blank=True, null=True)
    qty27 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr28 = models.PositiveIntegerField(blank=True, null=True)
    qty28 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr29 = models.PositiveIntegerField(blank=True, null=True)
    qty29 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr30 = models.PositiveIntegerField(blank=True, null=True)
    qty30 = models.PositiveSmallIntegerField(blank=True, null=True)
    mktslvr31 = models.PositiveIntegerField(blank=True, null=True)
    qty31 = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblItemHistoryMonthly'
        unique_together = (('item', 'house', 'level', 'month'),)


class Tblitemlevelsseen(models.Model):
    item = models.PositiveIntegerField(primary_key=True)
    bonusset = models.PositiveIntegerField()
    level = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tblItemLevelsSeen'
        unique_together = (('item', 'bonusset', 'level'),)


class Tblitemsummary(models.Model):
    house = models.PositiveSmallIntegerField(primary_key=True)
    item = models.IntegerField()
    level = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=11, decimal_places=0)
    quantity = models.PositiveIntegerField()
    lastseen = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblItemSummary'
        unique_together = (('house', 'item', 'level'),)


class Tblpet(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    json = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    type = models.PositiveIntegerField()
    icon = models.CharField(max_length=120)
    npc = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblPet'


class Tblpetglobal(models.Model):
    species = models.PositiveSmallIntegerField(primary_key=True)
    region = models.CharField(max_length=2)
    median = models.DecimalField(max_digits=11, decimal_places=0)
    mean = models.DecimalField(max_digits=11, decimal_places=0)
    stddev = models.DecimalField(max_digits=11, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'tblPetGlobal'
        unique_together = (('species', 'region'),)


class Tblpetsummary(models.Model):
    house = models.PositiveSmallIntegerField(primary_key=True)
    species = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=11, decimal_places=0)
    quantity = models.PositiveIntegerField()
    lastseen = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblPetSummary'
        unique_together = (('house', 'species'),)


class Tblrealm(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    region = models.CharField(max_length=2)
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    locale = models.CharField(max_length=5, blank=True, null=True)
    house = models.PositiveSmallIntegerField(blank=True, null=True)
    canonical = models.CharField(max_length=50, blank=True, null=True)
    ownerrealm = models.CharField(max_length=100, blank=True, null=True)
    population = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblRealm'
        unique_together = (('region', 'slug'), ('region', 'name'),)


class Tblsnapshot(models.Model):
    house = models.PositiveSmallIntegerField(primary_key=True)
    updated = models.DateTimeField()
    maxid = models.PositiveIntegerField(blank=True, null=True)
    flags = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'tblSnapshot'
        unique_together = (('house', 'updated'),)


class Tblwowtoken(models.Model):
    region = models.CharField(primary_key=True, max_length=2)
    when = models.DateTimeField()
    marketgold = models.PositiveIntegerField(blank=True, null=True)
    timeleft = models.CharField(max_length=9, blank=True, null=True)
    timeleftraw = models.PositiveIntegerField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblWowToken'
        unique_together = (('region', 'when'),)
