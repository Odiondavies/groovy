"""empty message

Revision ID: 1cee11b4f9d3
Revises: 
Create Date: 2024-07-25 05:52:39.525225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cee11b4f9d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('date_registered', sa.DateTime(), nullable=True),
    sa.Column('dp', sa.String(length=255), nullable=True),
    sa.Column('customer_type', sa.Enum('chef', 'caterer', 'agent', 'customer'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('agents',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('state', sa.String(length=30), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('specialities', sa.Text(), nullable=False),
    sa.Column('verification', sa.Enum('verified', 'unverified'), nullable=True),
    sa.Column('view_count', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('0', '1', '2'), nullable=True),
    sa.Column('date_registered', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customerid'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caterers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('state', sa.String(length=30), nullable=False),
    sa.Column('specialities', sa.Text(), nullable=False),
    sa.Column('working_days', sa.String(length=255), nullable=False),
    sa.Column('view_count', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('0', '1', '2'), nullable=True),
    sa.Column('verification', sa.Enum('verified', 'unverified'), nullable=True),
    sa.Column('date_registered', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customerid'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('chefs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('state', sa.String(length=30), nullable=False),
    sa.Column('specialities', sa.Text(), nullable=False),
    sa.Column('working_days', sa.String(length=200), nullable=False),
    sa.Column('view_count', sa.Integer(), nullable=True),
    sa.Column('verification', sa.Enum('verified', 'unverified'), nullable=True),
    sa.Column('status', sa.Enum('0', '1', '2'), nullable=True),
    sa.Column('date_registered', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customerid'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('ref', sa.String(length=255), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('date_paid', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('pending', 'failed', 'paid'), server_default='pending', nullable=True),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customerid'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('file', sa.String(length=255), nullable=False),
    sa.Column('file_type', sa.Enum('image', 'video'), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('likes_count', sa.Integer(), nullable=True),
    sa.Column('category', sa.Enum('chef', 'caterer'), nullable=False),
    sa.Column('posterid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['posterid'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('image', sa.Text(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('status', sa.Enum('0', '1'), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customerid'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('booking',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('chef', sa.Integer(), nullable=True),
    sa.Column('caterer', sa.Integer(), nullable=True),
    sa.Column('booker', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['booker'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['caterer'], ['caterers.id'], ),
    sa.ForeignKeyConstraint(['chef'], ['chefs.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('cart',
    sa.Column('cart_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.Column('productid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customerid'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['productid'], ['products.id'], ),
    sa.PrimaryKeyConstraint('cart_id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('comment_date', sa.DateTime(), nullable=True),
    sa.Column('commenterid', sa.Integer(), nullable=True),
    sa.Column('postid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['commenterid'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['postid'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gallery',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('image', sa.Text(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('catererid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['catererid'], ['caterers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('likes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('like_date', sa.DateTime(), nullable=True),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.Column('postid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customerid'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['postid'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_number', sa.String(length=255), nullable=False),
    sa.Column('date_ordered', sa.DateTime(), nullable=True),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.Column('paymentid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customerid'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['paymentid'], ['payment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wishlist',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('wishlist_date', sa.DateTime(), nullable=True),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.Column('productid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customerid'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['productid'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('orderid', sa.Integer(), nullable=True),
    sa.Column('productid', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price_per_unit', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['orderid'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['productid'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_item')
    op.drop_table('wishlist')
    op.drop_table('orders')
    op.drop_table('likes')
    op.drop_table('gallery')
    op.drop_table('comments')
    op.drop_table('cart')
    op.drop_table('booking')
    op.drop_table('products')
    op.drop_table('post')
    op.drop_table('payment')
    op.drop_table('chefs')
    op.drop_table('caterers')
    op.drop_table('agents')
    op.drop_table('customers')
    # ### end Alembic commands ###
