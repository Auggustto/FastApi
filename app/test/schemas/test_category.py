import pytest
from app.models.categories import Category

def test_category_schema():
    
    category = Category(
        name = 'Roupa',
        slug = 'roupa'
    )
    assert category.slug == 'roupa'
    
    category = Category(
        name='Roupa',
        slug='roupa-de-cama'
    )
    assert category.slug == 'roupa-de-cama'

    category = Category(
        name='Roupa',
        slug='roupa_de_cama'
    )
    assert category.slug == 'roupa_de_cama'
    
    
def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        Category(
            name = 'Roupa',
            slug = 'roupa de cama'
        )
        
    with pytest.raises(ValueError):
        Category(
            name = 'Roupa',
            slug = 'Ção'
        )
    
    with pytest.raises(ValueError):
        Category(
            name = 'Roupa',
            slug = 'roupa de cama'
        )
    
    with pytest.raises(ValueError):
        Category(
            name = 'Roupa',
            slug = 'Roupa'
        )