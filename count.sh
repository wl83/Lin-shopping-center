find backend/app frontend/src -name "*.py" -or -name "*.js" -or -name "*.vue" | xargs wc -l
find backend/app frontend/src -name "*.py" -or -name "*.js" -or -name "*.vue" | xargs cat | wc -l
echo py
find backend/app -name "*.py" | xargs cat | wc -l
echo frontend
find frontend/src -name "*.js" -or -name "*.vue" | xargs cat | wc -l
