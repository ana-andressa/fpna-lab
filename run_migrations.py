"""
ORQUESTRADOR: Executa todas as migrations

Este script:
1. Descobre todos os arquivos migration_*.py em migrations/
2. Executa cada função migration_*()
3. Registra sucesso ou erro
4. Mostra resumo final
"""

import os
import sys
import importlib.util
from datetime import datetime


def discover_migrations():
    """Descobre todas as migrations em migrations/"""
    migrations = []
    migrations_dir = "migrations"
    
    if not os.path.exists(migrations_dir):
        print(f"❌ Pasta {migrations_dir}/ não encontrada!")
        return migrations
    
    print(f"🔍 Procurando migrations em {migrations_dir}/...")
    
    for filename in sorted(os.listdir(migrations_dir)):
        if filename.endswith(".py") and not filename.startswith("_"):
            filepath = os.path.join(migrations_dir, filename)
            migrations.append((filename, filepath))
            print(f"  ✓ Encontrada: {filename}")
    
    return migrations


def run_migration(filepath, filename):
    """Executa uma migration"""
    try:
        # Importar arquivo como módulo
        spec = importlib.util.spec_from_file_location(filename, filepath)
        module = importlib.util.module_from_spec(spec)
        
        # Adicionar ao path para importar config/
        sys.path.insert(0, os.getcwd())
        
        spec.loader.exec_module(module)
        
        # Procurar função migration_*
        for attr_name in dir(module):
            if attr_name.startswith("migration_"):
                func = getattr(module, attr_name)
                if callable(func):
                    print(f"\n▶️  Executando: {attr_name}()")
                    result = func()
                    return result
        
        print(f"⚠️  Nenhuma função migration_* encontrada em {filename}")
        return False
    
    except Exception as e:
        print(f"❌ Erro ao executar {filename}: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Função principal"""
    print("\n" + "=" * 70)
    print("FP&A LAB - ORQUESTRADOR DE MIGRATIONS")
    print("=" * 70 + "\n")
    
    # Criar pasta outputs se não existir
    os.makedirs("outputs", exist_ok=True)
    
    # Descobrir migrations
    migrations = discover_migrations()
    
    if not migrations:
        print("\n⚠️  Nenhuma migration encontrada!")
        print("Crie arquivo em migrations/001_seu_relatorio.py")
        return
    
    print(f"\n📊 Total de migrations: {len(migrations)}\n")
    
    # Executar migrations
    results = []
    start_time = datetime.now()
    
    for i, (filename, filepath) in enumerate(migrations, 1):
        print(f"\n[{i}/{len(migrations)}] {filename}")
        print("-" * 70)
        
        success = run_migration(filepath, filename)
        results.append({
            "filename": filename,
            "success": success
        })
    
    # Resumo
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    successful = sum(1 for r in results if r["success"])
    failed = sum(1 for r in results if not r["success"])
    
    print("\n" + "=" * 70)
    print("RESUMO DE EXECUÇÃO")
    print("=" * 70)
    print(f"✓ Sucesso: {successful}/{len(results)}")
    print(f"✗ Falhas: {failed}/{len(results)}")
    print(f"⏱️  Tempo total: {duration:.2f}s")
    print("=" * 70)
    
    if failed == 0:
        print("\n🎉 TODAS AS MIGRATIONS EXECUTADAS COM SUCESSO!")
        print(f"📊 Outputs salvos em: outputs/")
        return 0
    else:
        print(f"\n⚠️  {failed} migration(s) falharam. Verifique os erros acima.")
        return 1


if __name__ == "__main__":
    exit_code = main() or 0
    sys.exit(exit_code)
