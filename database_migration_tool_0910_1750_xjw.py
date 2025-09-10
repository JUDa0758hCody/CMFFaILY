# 代码生成时间: 2025-09-10 17:50:55
import alembic.config
import alembic.command
import alembic.script
import sqlite3
import sys

# 定义数据库迁移工具类
class DatabaseMigrationTool:
    def __init__(self, database_url):
        """
        初始化数据库迁移工具
        
        :param database_url: 数据库连接URL
        """
        self.database_url = database_url
        self.alembic_cfg = self._create_alembic_cfg()

    def _create_alembic_cfg(self):
        """
        创建Alembic配置对象
        """
        cfg = alembic.config.Config()
        cfg.set_main_option("sqlalchemy.url", self.database_url)
        cfg.set_main_option("script_location", "alembic")
        return cfg

    def migrate_up(self):
        """
        执行数据库迁移
        """
        try:
            alembic.command.upgrade(self.alembic_cfg, "head")
            print("数据库迁移成功")
        except Exception as e:
            print(f"数据库迁移失败: {e}")
            sys.exit(1)

    def migrate_down(self, revision_id):
        """
        回滚数据库迁移
        
        :param revision_id: 回滚到的版本号
        "