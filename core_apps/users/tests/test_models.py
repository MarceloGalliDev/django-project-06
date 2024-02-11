import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_normal_user(normal_user):
    """
    testando funcionalidades do cadastro de usuario normal
    """
    assert normal_user.first_name is not None
    assert normal_user.last_name is not None
    assert normal_user.email is not None
    assert normal_user.password is not None
    assert normal_user.pkid is not None
    assert not normal_user.is_staff
    assert not normal_user.is_superuser
    assert normal_user.is_active


@pytest.mark.django_db
def test_create_super_user(super_user):
    """
    testando funcionalidades do cadastro de usuario admin
    """
    assert super_user.first_name is not None
    assert super_user.last_name is not None
    assert super_user.email is not None
    assert super_user.password is not None
    assert super_user.pkid is not None
    assert super_user.is_staff
    assert super_user.is_superuser
    assert super_user.is_active


@pytest.mark.django_db
def test_get_full_name(normal_user):
    """
    testando funcionalidades do full name no cadastro
    """
    full_name = normal_user.get_full_name
    expected_full_name = (
        f"{normal_user.first_name.title()} {normal_user.last_name.title()}"
    )
    assert full_name == expected_full_name


@pytest.mark.django_db
def test_get_short_name(normal_user):
    """
    testando funcionalidades do short name no cadastro
    """
    short_name = normal_user.get_short_name
    assert short_name == normal_user.first_name


@pytest.mark.django_db
def test_update_user(normal_user):
    """
    testando funcionalidades do short name no cadastro
    """
    new_first_name = "Jose"
    new_last_name = "Doe"
    normal_user.first_name = new_first_name
    normal_user.last_name = new_last_name
    normal_user.save()

    update_user = User.objects.get(pk=normal_user.pk)
    assert update_user.first_name == new_first_name
    assert update_user.last_name == new_last_name


@pytest.mark.django_db
def test_delete_user(normal_user):
    """
    testando funcionalidades de delete user no cadastro
    """
    user_pk = normal_user.pk
    normal_user.delete()

    with pytest.raises(User.DoesNotExist):
        User.objects.get(pk=user_pk)


@pytest.mark.django_db
def test_user_str(normal_user):
    """
    testando funcionalidades de __str__ user no cadastro
    """
    assert str(normal_user) == f"{normal_user.first_name}"


@pytest.mark.django_db
def test_normal_user_email_is_normalized(normal_user):
    """
    testando funcionalidades de email normalizado no cadastro
    """
    email = normal_user.email
    assert email == email.lower()


@pytest.mark.django_db
def test_super_user_email_is_normalized(super_user):
    """
    testando funcionalidades de email normalizado no cadastro
    """
    email = super_user.email
    assert email == email.lower()


@pytest.mark.django_db
def test_user_email_is_incorrect(user_factory):
    """
    testando funcionalidades de email invalido
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(email="testeemail.com")
    assert str(err.value) == "You must provider a valid email!"


@pytest.mark.django_db
def test_create_user_with_no_first_name(user_factory):
    """
    testando funcionalidades de criação de usuario invalido
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "Users must have a first name."


@pytest.mark.django_db
def test_create_user_with_no_last_name(user_factory):
    """
    testando funcionalidades de criação de usuario invalido
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "Users must have a last name."


@pytest.mark.django_db
def test_create_user_with_no_email(user_factory):
    """
    testando funcionalidades de criação de usuario invalido
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Users must have a valid e-mail."


@pytest.mark.django_db
def test_create_superuser_with_no_email(user_factory):
    """
    testando funcionalidades de criação de super usuario invalido
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Superuser must have an email"


@pytest.mark.django_db
def test_create_superuser_with_no_password(user_factory):
    """
    testando funcionalidades de criação de super usuario invalido
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(password=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Superuser must have password"


@pytest.mark.django_db
def test_create_superuser_is_not_staff(user_factory):
    """
    testando funcionalidades de criação de super usuario invalido
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "Superuser must have is_staff=True"


@pytest.mark.django_db
def test_create_superuser_is_not_superuser(user_factory):
    """
    testando funcionalidades de criação de super usuario invalido
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=True)
    assert str(err.value) == "Superuser must have is_superuser=True"
